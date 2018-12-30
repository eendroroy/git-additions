import os

import pygit2

from git_additions.__helpers import duration, commit_date, find_toplevel
from git_additions.exporter.csv_exporter import CSVExporter
from git_additions.logs.print_log import PrintLog


class Logs(object):

    def __init__(self, author=None, email=None, export=False, output=None):
        self.lines = []
        self.export = export
        self.output = output
        self.author = author
        self.email = email
        if export:
            self.exportet = CSVExporter()

    def run(self):

        last_commit = None
        first_commit = None

        repo = pygit2.Repository('%s/.git' % find_toplevel(os.getcwd()))
        for commit in repo.walk(repo.head.target, pygit2.GIT_SORT_TOPOLOGICAL | pygit2.GIT_SORT_REVERSE):
            if self.author is not None and commit.author.name != self.author:
                continue
            if self.email is not None and commit.author.email != self.email:
                continue
            line = [commit_date(commit), commit.author.name, commit.author.email]
            if last_commit is not None:
                dur = duration(last_commit, commit)
                line.append('%d %02d:%02d:%02d' % dur)
            else:
                line.append('0 00:00:00')
            line.append(commit.message.strip())
            if first_commit is None:
                first_commit = commit
            last_commit = commit
            self.lines.append(line)

        if self.export:
            headers = ['Time', 'Author', 'Email', 'Duration', 'Message']
            self.exportet.set_lines([headers] + self.lines)
            self.exportet.write_content(self.output)
        else:
            PrintLog(self.lines).run()
