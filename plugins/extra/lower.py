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

    def configure(resoqu):
        """_summary_
        """
        print("    called LowerPlugin::configure")
        resoqu.message = resoqu.message.lower()
        resoqu.message += '!'
