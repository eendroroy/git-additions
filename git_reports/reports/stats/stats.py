import time

import os
from pygit2 import Repository, GIT_SORT_TOPOLOGICAL, GIT_SORT_REVERSE

from git_reports.reports.__helpers import duration


class Stats(object):

    def __init__(self):
        pass

    def run(self):
        last_commit = None
        first_commit = None
        days = 0
        hours = 0
        minutes = 0
        seconds = 0

        repo = Repository('%s/.git' % os.getcwd())
        for commit in repo.walk(repo.head.target, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
            if last_commit is not None:
                dur = duration(last_commit, commit)
                if dur[0] < 1 and dur[1] < 8:
                    days += dur[0]
                    hours += dur[1]
                    minutes += dur[2]
                    seconds += dur[3]
            if first_commit is None:
                first_commit = commit
            last_commit = commit

        minutes += int(seconds / 60)
        seconds = int(seconds % 60)

        hours += int(minutes / 60)
        minutes = int(minutes % 60)

        days += int(hours / 24)
        hours = int(hours % 24)

        total_hours = (days * 24) + hours + (minutes / 60)

        print('     D HH:MM:SS')
        print('%6d %2d:%d:%d' % (days, hours, minutes, seconds))
        print()
        print('Total Work Hours (estimated): %f' % total_hours)
        print('Project Duration: %d %2d:%d:%d' % duration(first_commit, last_commit))
