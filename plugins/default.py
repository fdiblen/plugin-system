"""_summary_
"""

class DefaultPlugin:
    """
    _summary_
    """

    name = 'DefaultPlugin'

    def __init__(self, description=None) -> None:
        """_summary_
        """
        print("    called DefaultPlugin::__init__")
        self.description = description

    def configure(plugin_example):
        """_summary_
        """
        print("    called DefaultPlugin::configure")
        plugin_example.message = plugin_example.message.upper()

    def evaluate(plugin_example):
        """_summary_
        """
        print("    called DefaultPlugin::evaluate")
        print(plugin_example.message)
