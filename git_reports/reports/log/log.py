import os

from pygit2 import Repository, GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE

from git_reports.reports.__helpers import duration, commit_date
from git_reports.reports.exporter.csv_exporter import CSVExporter
from git_reports.reports.log.print_log import PrintLog


class Log(object):

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

        repo = Repository('%s/.git' % os.getcwd())
        for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
            if self.author is not None and commit.author.name != self.author:
                continue
            if self.email is not None and commit.author.email != self.email:
                continue
            line = [commit.author.name, commit.author.email, commit_date(commit), commit.message.strip()]
            if last_commit is not None:
                dur = duration(last_commit, commit)
                line.append('%d %d:%d:%d' % dur)
            if first_commit is None:
                first_commit = commit
            last_commit = commit
            self.lines.append(line)

        if self.export:
            headers = ['Author', 'Email', 'Time', 'Message', 'Duration']
            self.exportet.set_lines([headers] + self.lines)
            self.exportet.write_content(self.output)
        else:
            PrintLog(self.lines).run()
