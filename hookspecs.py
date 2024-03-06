"""_summary_
"""

import os
import json
import inspect
import pluggy
from config import CONFIG_FILES

from constants import PROJECT_NAME, hook_spec, hook_impl
from defaults import default_plugins, default_config


class PluginSystem:
    """
    _summary_
    """

    def __init__(self, message="", plugins=None) -> None:
        """
        _summary_
        """
        print("called PluginSystem::__init__")
        self.message = message
        self.plugins = plugins
        self.config = self.get_config()
        self.pm = self.get_plugin_manager(plugins)

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
        self.pm.hook.configure(plugin_example=self)
        self.pm.hook.evaluate(plugin_example=self)
        return self.message

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

    def run_specified(self):
        """ more controlled effort - quick hack as poc """
        for func_name in self.confs['process_data_steps']:
            # find function in module
            for plugin_name, plugin_module in  \
                            self.pm.list_name_plugin():
                if func_name in dir(plugin_module):
                    print(getattr(self.pm.get_plugin(plugin_name),
                        func_name)(csv='passed in csv'))


class PluginSystemSpecs:
    """
    This is where we spec out our frameworks plugins, I like to refer to them as
    the lifecycle.  Each of these functions is a plugin that we are exposing to
    our users, with the kwargs that we expect to pass them.
    """
    @hook_spec
    def configure(self, plugin_example: PluginSystem) -> None:
        """
        The first hook that runs.
        """
        pass

    @hook_spec
    def evaluate(self, plugin_example: PluginSystem) -> None:
        """
        The last hook that runs.
        """
        pass
