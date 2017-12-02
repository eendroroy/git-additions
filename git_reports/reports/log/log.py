import time

import os
from pygit2 import Repository, GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE

from git_reports.reports.__helpers import duration, commit_date
from git_reports.reports.exporter.csv_exporter import CSVExporter


class Log(object):

    def __init__(self, export=False, output=None):
        self.exportet = CSVExporter()
        self.export = export
        self.output = output

    @staticmethod
    def printer(obj):
        print(obj, end='', flush=True)

    def run(self):

        last_commit = None
        first_commit = None

        repo = Repository('%s/.git' % os.getcwd())
        for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
            if not self.export:
                self.printer(commit.author.name)
                self.printer(' ==> ')
                self.printer(commit_date(commit))
                self.printer(' ==> ')
                self.printer(commit.message.strip())
            if self.export:
                line = [commit.author.name, commit_date(commit), commit.message.strip()]
            if last_commit is not None:
                if not self.export:
                    self.printer(' ==> ')
                dur = duration(last_commit, commit)
                if not self.export:
                    self.printer('%d %d:%d:%d' % dur)
                if self.export:
                    line.append('%d %d:%d:%d' % dur)
            if first_commit is None:
                first_commit = commit
            last_commit = commit
            if not self.export:
                print()
            if self.export:
                self.exportet.add_line(line)

        if self.export:
            self.exportet.write_content(self.output)
