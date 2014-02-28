import subprocess


class Programme(object):
    """
    Holds all the attributes of a programme.
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)


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
        programmes = []
        output = subprocess.check_output([self.executable])
        for line in output:
            programmes.append(Programme())
