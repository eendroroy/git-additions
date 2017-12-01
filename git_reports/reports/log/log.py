import time

import os
from pygit2 import Repository, GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE

from git_reports.reports.__helpers import duration, commit_date


class Log(object):

    def __init__(self):
        pass

    @staticmethod
    def printer(obj):
        print(obj, end='', flush=True)

    def run(self):

        last_commit = None
        first_commit = None

        repo = Repository('%s/.git' % os.getcwd())
        for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
            self.printer(commit.author.name)
            self.printer(' ==> ')
            self.printer(commit_date(commit))
            self.printer(' ==> ')
            self.printer(commit.message.strip())
            if last_commit is not None:
                self.printer(' ==> ')
                dur = duration(last_commit, commit)
                self.printer('%d %d:%d:%d' % dur)
            if first_commit is None:
                first_commit = commit
            last_commit = commit
            print()
