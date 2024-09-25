"""_summary_
"""

from hookspecs import PluginSystem, discover_extra_plugins


def main():
    """_summary_
    """

    app = PluginSystem(
        message="hello worldS!",
        plugins=discover_extra_plugins()
    )

    app.show_config()
    app.list_plugins()
    final_result = app.run()
    # app.run_specified()  # evaluate based on configs order

    print("")
    print('Result:', final_result)


if __name__ == "__main__":
    main()
