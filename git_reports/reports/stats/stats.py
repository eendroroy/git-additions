import os
from optparse import OptionParser

import pygit2
from colorama import Fore, Style

from git_reports.reports.__helpers import find_toplevel


class Stats(object):

    def __init__(self, options):
        self.__options = options
        print(options)

    def report(self):
        repo = pygit2.Repository('%s/.git' % find_toplevel(os.getcwd()))
        previous_commit = None
        for commit in repo.walk(repo.head.target, pygit2.GIT_SORT_TOPOLOGICAL | pygit2.GIT_SORT_REVERSE):
            if previous_commit is not None:
                diff = commit.tree.diff_to_tree(previous_commit.tree)
                print('#%s%s' % (Fore.CYAN, commit.short_id), end='\t')
                print(
                    '%s%s%s <%s>%s' % (Fore.YELLOW, commit.author.name, Style.DIM, commit.author.email, Style.NORMAL),
                    end='\t'
                )
                print('%sf: %s' % (Fore.BLUE, diff.stats.files_changed), end='\t')
                print('%s+: %s' % (Fore.GREEN, diff.stats.insertions,), end='\t')
                print('%s-: %s' % (Fore.RED, diff.stats.deletions,), end='\t')
                if self.__options.message:
                    print('%s%s' % (Fore.LIGHTBLUE_EX, str(commit.message).strip()), end='\t')
                print(Style.RESET_ALL)
            previous_commit = commit
