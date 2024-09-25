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

    def configure(resoqu):
        """_summary_
        """
        print("    called NoDecoratorPlugin::configure")
        resoqu.message += '-'

    def evaluate(resoqu):
        """_summary_
        """
        print("    called NoDecoratorPlugin::evaluate")
        resoqu.message += '*'
