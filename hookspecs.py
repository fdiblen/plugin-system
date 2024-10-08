"""_summary_
"""

import os
import json
import inspect
import yaml
import pluggy
from config import CONFIG_FILES

from constants import PROJECT_NAME, hook_spec, hook_impl
from defaults import default_plugins, default_config

from utils.git_utils import checkout_subfolders
from models.assesment import MainModel

from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module

class PluginSystem:
    """
    _summary_
    """

    def __init__(self, assesment: MainModel = None, message="", code_path="./", plugins=None) -> None:
        """
        _summary_
        """
        print("called PluginSystem::__init__")
        self.download_online_plugins()
        self.message = message
        self.code_path = code_path
        self.assesment = assesment
        self.plugins = plugins
        self.config = self.get_config()
        self.pm = self.get_plugin_manager(plugins)


    def download_online_plugins(self):
        """_summary_
        """
        print("")
        print("called PluginSystem::get_online_plugins")
        with open('plugin-config.yaml', 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)

        # print(config)

        for __registry in config['registry']:
            # print(__registry)

            if __registry['plugins']:
                registry_url = __registry['url']
                registry_name = __registry['name']
                branch_name = __registry['branch']
                plugin_list = __registry['plugins']

                checkout_subfolders(
                    repo_url=registry_url,
                    target_folder=f"plugins/{registry_name}",
                    branch=branch_name,
                    sub_folders=plugin_list
                )

    def get_config(self):
        """__summary__
        """
        print("called PluginSystem::get_config")
        config = {}
        for cfile in CONFIG_FILES:
            if not os.path.isfile(cfile):
                print("    Cannot find a config file, creating an empty one...")
                config.update(default_config)
                # TODO: add save_config function
                json_config = json.dumps(default_config)
                with open(cfile, encoding='utf-8', mode='w') as json_file:
                    json_file.write(json_config)
                    print("    Successfully saved the config file.")
            else:
                print(f'    Reading config file {cfile}')
                with open(cfile, encoding='utf-8', mode='r') as f:
                    config.update(json.load(f))
        return config

    def get_plugin_manager(self, plugins=None):
        """_summary_
        """
        print("")
        print("called PluginSystem::get_plugin_manager")
        pm = pluggy.PluginManager(PROJECT_NAME)
        pm.add_hookspecs(PluginSystemSpecs)
        # pm.load_setuptools_entrypoints(PROJECT_NAME)

        print('    Registering default plugins:')
        for plugin in default_plugins:
            for name, fn in inspect.getmembers(plugin, inspect.isfunction):
                if name in ['configure', 'evaluate']:
                    setattr(plugin, name, hook_impl(fn))
            print(f'        {plugin.name}')
            pm.register(plugin)

        if plugins:
            print('    Registering extra plugins:')
            for plugin in plugins:
                # if plugin.name == 'NoDecoratorPlugin':
                #     # print('        skipping: NoDecoratorPlugin')
                #     for name, fn in inspect.getmembers(plugin, inspect.isfunction):
                #         # print(f'name:{name}  fn:{fn}')
                #         if name in ['configure', 'evaluate']:
                #             setattr(plugin, name, hook_impl(fn))
                # else:
                #     print(f'        {plugin.name}')
                #     pm.register(plugin)

                # add @hook_impl decorator to class methods
                for name, fn in inspect.getmembers(plugin, inspect.isfunction):
                    if name in ['configure', 'evaluate']:
                        setattr(plugin, name, hook_impl(fn))
                print(f'        {plugin.name}')
                pm.register(plugin)
            print()

        return pm

    def run(self):
        """
        _summary_
        """
        print("called PluginSystem::run")
        self.pm.hook.configure(resoqu=self)
        self.pm.hook.evaluate(resoqu=self)
        return {
            "message": self.message,
            "code_path": self.code_path,
            "assesment": self.assesment
        }

    def run_specified(self):
        """ more controlled effort - quick hack as poc """
        for func_name in self.confs['process_data_steps']:
            # find function in module
            for plugin_name, plugin_module in  \
                            self.pm.list_name_plugin():
                if func_name in dir(plugin_module):
                    print(getattr(self.pm.get_plugin(plugin_name),
                        func_name)(csv='passed in csv'))

    def list_plugins(self):
        """__summary__"""
        print("called PluginSystem::list_plugins")
        for plugin_name, plugin_module in self.pm.list_name_plugin():
            print(f'    plugin_name: {plugin_name} plugin_module: {plugin_module}')
        print()

    def show_config(self):
        """__summary__"""
        print("called PluginSystem::show_config")
        print(f'    config: {self.config}')
        print()


class PluginSystemSpecs:
    """
    This is where we spec out our frameworks plugins, I like to refer to them as
    the lifecycle.  Each of these functions is a plugin that we are exposing to
    our users, with the kwargs that we expect to pass them.
    """
    @hook_spec
    def configure(self, resoqu: PluginSystem) -> None:
        """
        The first hook that runs.
        """
        pass

    @hook_spec
    def evaluate(self, resoqu: PluginSystem) -> None:
        """
        The last hook that runs.
        """
        pass


def discover_extra_plugins():
    plugin_class_list = {}

    package_dir = Path("plugins/extra").resolve()
    # print(package_dir)
    for (_, module_name, _) in iter_modules([package_dir]):
        # import the module and iterate through its attributes
        module = import_module(f"plugins.extra.{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)

            if isclass(attribute):
                # Add the class to this package's variables
                globals()[attribute_name] = attribute

                # print("    ", attribute_name, attribute)
                plugin_class_list[attribute_name] = attribute.__module__

    # print(sys.modules.keys())
    # print("dir: ", dir())
    # print("globals: ", globals())
    # print("locals: ", locals())

    # print(plugin_class_list)

    available_plugin_classes = []
    for class_name, module_name in plugin_class_list.items():
        available_plugin_classes.append(getattr(import_module(module_name), class_name))

    return available_plugin_classes
