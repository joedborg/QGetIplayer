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

    def getProgrammes(self, keywords=[], categories=[], channels=[], exclude_keywords=[], exclude_categories=[], exclude_channels=[]):
        """
        Return a filtered list of programmes.
        """
        programmes = []
        execute = [self.executable]
        if keywords:
            execute.append(','.join(keywords))
        if catergories:
            execute.append('--catergories')
            execute.append(','.join(catergories))
        if channels:
            execute.append('--channels')
            execute.append(','.join(channels))
        if exclude_keywords:
            execute.append('--exclude')
            execute.append(','.join(exclude_keywords))
        if exclude_catergories:
            execute.append('--exclude-catergory')
            execute.append(','.join(exclude_catergories))
        if exclude_channel:
            execute.append('--exclude-channel')
            execute.append(','.join(execlude_channel))

        proc = subprocess.Popen(execute, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = proc.read()
        for line in output:
            programmes.append(Programme(line.split()))
