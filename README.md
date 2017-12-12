# git-reports

[![GitHub tag](https://img.shields.io/github/tag/eendroroy/git-reports.svg)](https://github.com/eendroroy/git-reports/tags)
[![PyPI](https://img.shields.io/pypi/v/git-reports.svg)](https://pypi.python.org/pypi/git-reports/)
[![PyPI](https://img.shields.io/pypi/pyversions/git-reports.svg)](https://pypi.python.org/pypi/git-reports)

[![Contributors](https://img.shields.io/github/contributors/eendroroy/git-reports.svg)](https://github.com/eendroroy/git-reports/graphs/contributors)
[![GitHub last commit (branch)](https://img.shields.io/github/last-commit/eendroroy/git-reports/master.svg)](https://github.com/eendroroy/git-reports)
[![license](https://img.shields.io/github/license/eendroroy/git-reports.svg)](https://github.com/eendroroy/git-reports/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/eendroroy/git-reports.svg)](https://github.com/eendroroy/git-reports/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/eendroroy/git-reports.svg)](https://github.com/eendroroy/git-reports/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/eendroroy/git-reports.svg)](https://github.com/eendroroy/git-reports/pulls)
[![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/eendroroy/git-reports.svg)](https://github.com/eendroroy/git-reports/pulls?q=is%3Apr+is%3Aclosed)

## Reports

**Usage**

```
Usage: git report {report-name} [options]

Options:
  -h, --help            show this help message and exit
  -o FILE, --out-file=FILE
                        write report to FILE
  -a AUTHOR, --author=AUTHOR
                        filter by author name
  -e EMAIL, --email=EMAIL
                        filter by author email
```

**Log**

```
$ git report log [-o report.csv] [-a indrajit] [-e eendroroy@gmail.com]
```

```
indrajit ==> Thu Nov 30 21:50:50 2017 ==> initial commit
indrajit ==> Thu Nov 30 21:56:41 2017 ==> requirements ==> 0 0:5:51
indrajit ==> Fri Dec  1 23:32:53 2017 ==> configs ==> 1 1:36:12
indrajit ==> Fri Dec  1 23:33:33 2017 ==> setup configs ==> 0 0:0:40
indrajit ==> Fri Dec  1 23:58:52 2017 ==> setup configs ==> 0 0:25:19
indrajit ==> Sat Dec  2 00:02:36 2017 ==> git_reports ==> 0 0:3:44
indrajit ==> Sat Dec  2 01:59:27 2017 ==> configs ==> 0 1:56:51
indrajit ==> Sat Dec  2 02:01:08 2017 ==> reports ==> 0 0:1:41
indrajit ==> Sat Dec  2 02:01:46 2017 ==> reports log ==> 0 0:0:38
indrajit ==> Sat Dec  2 02:02:17 2017 ==> reports stats ==> 0 0:0:31
```

**Stats**

```
$ git report stats
```

```
     D HH:MM:SS
     0  4:16:56

Total Work Hours (estimated): 4.266667
Project Duration: 1 17:49:59
```

**Users**

```
$ git report users
```

## Contributing

Bug reports and pull requests are welcome on GitHub at [git-reports](https://github.com/eendroroy/git-reports) repository.
This project is intended to be a safe, welcoming space for collaboration,
and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Author

* **indrajit** - *Owner* - [eendroroy](https://github.com/eendroroy)

## License

The project is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).