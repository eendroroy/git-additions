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

    def run(self):
        (options, args) = self.parser.parse_args()
        report_name = args[0]
        if report_name == 'log':
            if options.output is not None:
                Log(export=True, output=options.output).run()
            else:
                Log().run()
        if report_name == 'stats':
            Stats().run()
        try:
            sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(1)
