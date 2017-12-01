#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from git_reports.reports.log.log import Log


class Cli(object):
    @staticmethod
    def run():
        report_name = sys.argv[1]
        if report_name == 'log':
            Log().run()
        try:
            sys.exit(0)
        except KeyboardInterrupt:
            sys.exit(1)
