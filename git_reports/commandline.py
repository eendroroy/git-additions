#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from optparse import OptionParser

from git_reports.reports.log.log import Log
from git_reports.reports.stats.stats import Stats


class Cli(object):

    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option(
            "-o", "--out-file", dest="output", help="write report to FILE", metavar="FILE"
        )
        self.parser.add_option(
            "-a", "--author", dest="author", help="filter by author name", metavar="AUTHOR"
        )
        self.parser.add_option(
            "-e", "--email", dest="email", help="filter by author email", metavar="EMAIL"
        )

    def run(self):
        (options, args) = self.parser.parse_args()
        if len(args) != 1:
            self.parser.error("wrong number of arguments")
        if args[0] == 'log':
            author = options.author
            email = options.email
            if options.output is not None:
                Log(author, email, True, options.output).run()
            else:
                Log(author, email).run()
        elif args[0] == 'stats':
            Stats().run()
        else:
            print('Unknown report "%s"' % args[0])
            exit(1)
        try:
            sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(1)
