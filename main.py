"""_summary_
"""

from hookspecs import PluginSystem

# from plugins.lower import LowerPlugin
# from plugins.no_decorator import NoDecoratorPlugin

from inspect import isclass
from pkgutil import iter_modules
from pathlib import Path
from importlib import import_module

import sys

def main():
    """_summary_
    """

    plugin_class_list = {}

    package_dir = Path("plugins/extra").resolve()
    print(package_dir)
    for (_, module_name, _) in iter_modules([package_dir]):
        # import the module and iterate through its attributes
        module = import_module(f"plugins.extra.{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)

            if isclass(attribute):
                # Add the class to this package's variables
                globals()[attribute_name] = attribute

                print("    ", attribute_name, attribute)
                plugin_class_list[attribute_name] = attribute.__module__

    # print(sys.modules.keys())
    # print("dir: ", dir())
    # print("globals: ", globals())
    # print("locals: ", locals())

    print(plugin_class_list)

    plugin_classes = []
    for className, moduleName in plugin_class_list.items():
        plugin_classes.append(getattr(import_module(moduleName), className))

    app = PluginSystem(
        message="hello worldS!",
        # plugins=[
        #     # LowerPlugin,
        #     # NoDecoratorPlugin,
        # ]
        plugins=plugin_classes
    )

    app.show_config()
    app.list_plugins()
    app.run()
    # app.run_specified()  # evaluate based on configs order


if __name__ == "__main__":
    main()
