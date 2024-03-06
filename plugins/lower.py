"""_summary_
"""

class LowerPlugin:
    """
    _summary_
    """

    name = 'LowerPlugin'

    def __init__(description=None) -> None:
        """_summary_
        """
        print("    called LowerPlugin::__init__")
        self.description = description

    def configure(plugin_example):
        """_summary_
        """
        print("    called LowerPlugin::configure")
        plugin_example.message = plugin_example.message.lower()
        plugin_example.message += '!'
