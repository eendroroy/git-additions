# git-additions

[![GitHub tag](https://img.shields.io/github/tag/eendroroy/git-additions.svg)](https://github.com/eendroroy/git-additions/tags)
[![PyPI](https://img.shields.io/pypi/v/git-additions.svg)](https://pypi.python.org/pypi/git-additions/)
[![PyPI](https://img.shields.io/pypi/pyversions/git-additions.svg)](https://pypi.python.org/pypi/git-additions)

[![Contributors](https://img.shields.io/github/contributors/eendroroy/git-additions.svg)](https://github.com/eendroroy/git-additions/graphs/contributors)
[![GitHub last commit (branch)](https://img.shields.io/github/last-commit/eendroroy/git-additions/master.svg)](https://github.com/eendroroy/git-additions)
[![license](https://img.shields.io/github/license/eendroroy/git-additions.svg)](https://github.com/eendroroy/git-additions/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/eendroroy/git-additions.svg)](https://github.com/eendroroy/git-additions/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/eendroroy/git-additions.svg)](https://github.com/eendroroy/git-additions/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/eendroroy/git-additions.svg)](https://github.com/eendroroy/git-additions/pulls)
[![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/eendroroy/git-additions.svg)](https://github.com/eendroroy/git-additions/pulls?q=is%3Apr+is%3Aclosed)

## Usage

```bash
$ git duration
     D HH:MM:SS
     0 16:1:54

Total Work Hours (estimated): 16.031667
Project Duration: 394  1:20:5
```

```bash
$ git logs -h
Usage: git-logs [options]

Options:
  -h, --help            show this help message and exit
  -o FILE, --out-file=FILE
                        write report to FILE
  -a AUTHOR, --author=AUTHOR
                        filter by author name
  -e EMAIL, --email=EMAIL
                        filter by author email
```

```bash
$ git stats -h
Usage: git-stats [options]

Options:
  -h, --help     show this help message and exit
  -m, --message  Show Commit Message
  -s, --short    Show Short Stat
```

```bash
$ git users
Name     	 Email               	 Commits
________ 	 ___________________ 	 _______
indrajit 	 eendroroy@gmail.com 	 54
```

## Author

* **indrajit** - *Owner* - [eendroroy](https://github.com/eendroroy)

## Contributing

Bug additions and pull requests are welcome on GitHub at [git-additions](https://github.com/eendroroy/git-additions) repository.
This project is intended to be a safe, welcoming space for collaboration,
and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

  1. Fork it ( https://github.com/eendroroy/git-additions/fork )
  1. Create your feature branch (`git checkout -b my-new-feature`)
  1. Commit your changes (`git commit -am 'Add some feature'`)
  1. Push to the branch (`git push origin my-new-feature`)
  1. Create a new Pull Request

## License

The project is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).