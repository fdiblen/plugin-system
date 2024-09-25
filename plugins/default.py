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

    def configure(resoqu):
        """_summary_
        """
        print("    called DefaultPlugin::configure")
        resoqu.message = resoqu.message.upper()

    def evaluate(resoqu):
        """_summary_
        """
        print("    called DefaultPlugin::evaluate")
        print(resoqu.message)
