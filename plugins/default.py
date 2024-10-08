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
        print("")
        print("    called DefaultPlugin::__init__")
        self.description = description

    def configure(resoqu):
        """_summary_
        """
        print("")
        print("    called DefaultPlugin::configure")
        resoqu.message = resoqu.message.upper()
        print('    resoqu.code_path: ', resoqu.code_path)
        print('    resoqu.assesment: ', resoqu.assesment)


    def evaluate(resoqu):
        """_summary_
        """
        print("")
        print("    called DefaultPlugin::evaluate")
        print('    DefaultPlugin --> resoqu.message: ', resoqu.message)
        print('    DefaultPlugin --> resoqu.code_path: ', resoqu.code_path)
        print('    DefaultPlugin --> resoqu.assesment: ', resoqu.assesment)
