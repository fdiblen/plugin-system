"""_summary_
"""


class NoDecoratorPlugin:
    """
    _summary_
    """

    name = 'NoDecoratorPlugin'

    def __init__(self, description=None) -> None:
        """_summary_
        """
        print("    called NoDecoratorPlugin::__init__")
        self.description = description

    def configure(plugin_example):
        """_summary_
        """
        print("    called NoDecoratorPlugin::configure")
        plugin_example.message += '-'

    def evaluate(plugin_example):
        """_summary_
        """
        print("    called NoDecoratorPlugin::evaluate")
        plugin_example.message += '*'
