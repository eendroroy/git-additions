import os

import pygit2
from colorama import Fore, Style

from git_reports.reports.__helpers import find_toplevel


class Stats(object):

    def __init__(self, options):
        self.__options = options

    def report(self):
        repo = pygit2.Repository('%s/.git' % find_toplevel(os.getcwd()))
        if self.__options.short:
            self.short(repo)
        else:
            self.stats(repo)

    def stats(self, repo):
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

    @staticmethod
    def short(repo):
        previous_commit = None
        report = dict()
        for commit in repo.walk(repo.head.target, pygit2.GIT_SORT_TOPOLOGICAL | pygit2.GIT_SORT_REVERSE):
            if previous_commit is not None:
                diff = commit.tree.diff_to_tree(previous_commit.tree)
                key = '%s-%s' % (commit.author.name, commit.author.email)
                if key not in report.keys():
                    report[key] = {'files_changed': 0, 'insertions': 0, 'deletions': 0}

                report[key]['files_changed'] += diff.stats.files_changed
                report[key]['insertions'] += diff.stats.insertions
                report[key]['deletions'] += diff.stats.deletions
            previous_commit = commit
        for key in report.keys():
            author = str(key).split('-')
            print(
                '%s%s%s <%s>%s' % (Fore.YELLOW, author[0], Style.DIM, author[1], Style.NORMAL),
                end='\t'
            )
            print('%sf: %s' % (Fore.BLUE, report[key]['files_changed']), end='\t')
            print('%s+: %s' % (Fore.GREEN, report[key]['insertions']), end='\t')
            print('%s-: %s' % (Fore.RED, report[key]['deletions']))
