from optparse import OptionParser

from git_reports.reports.stats.stats import Stats


def runner():
    parser = OptionParser()
    parser.add_option(
        "-m", "--message", action="store_true", dest="message", default=False, help="show message"
    )
    (options, args) = parser.parse_args()
    Stats(options).report()
