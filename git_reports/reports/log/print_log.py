class PrintLog(object):

    def __init__(self, lines):
        self.lines = lines

    def run(self):
        for line in self.lines:
            print(' ==> '.join(line))
