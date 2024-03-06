"""_summary_
"""

from hookspecs import PluginSystem

from plugins.lower import LowerPlugin
from plugins.no_decorator import NoDecoratorPlugin


def main():
    """_summary_
    """
    app = PluginSystem(
        message="hello worldS!",
        plugins=[
            LowerPlugin,
            NoDecoratorPlugin,
        ],
    )

    app.show_config()
    app.list_plugins()
    app.run()
    # app.run_specified()  # evaluate based on configs order



if __name__ == "__main__":
    main()
