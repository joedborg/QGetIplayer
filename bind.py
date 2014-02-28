import subprocess

class GetIplayerBind(object):
    """
    Bind to the get_iplayer Perl script.
    """
    def __init__(self):
        """
        Find the executable.
        """
        self.executable = "/home/joe/Projects/get_iplayer/get_iplayer"

    def getAllProgrammes(self):
        """
        Return all the programmes.
        """
