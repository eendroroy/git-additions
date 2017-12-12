git-reports
===========

|Contributors| |GitHub last commit (branch)| |license| |GitHub issues| |GitHub closed issues| |GitHub pull requests| |GitHub closed pull requests|

Reports
-------

**Usage**

::

    Usage: git report [options]

    Options:
      -h, --help            show this help message and exit
      -o FILE, --out-file=FILE
                            write report to FILE
      -a AUTHOR, --author=AUTHOR
                            filter by author name
      -e EMAIL, --email=EMAIL
                            filter by author email

**Log**

::

    $ git report log [-o report.csv] [-a indrajit] [-e eendroroy@gmail.com]

**Stats**

::

    $ git report stats

**Users**

::

    $ git report users

Contributing
------------

Bug reports and pull requests are welcome on GitHub at
`git-reports <https://github.com/eendroroy/git-reports>`__ repository.
This project is intended to be a safe, welcoming space for
collaboration, and contributors are expected to adhere to the
`Contributor Covenant <http://contributor-covenant.org>`__ code of
conduct.

Author
------

-  **indrajit** - *Owner* - `eendroroy <https://github.com/eendroroy>`__

License
-------

The project is available as open source under the terms of the `MIT
License <http://opensource.org/licenses/MIT>`__.


.. |Contributors| image:: https://img.shields.io/github/contributors/eendroroy/git-reports.svg
   :target: https://github.com/eendroroy/git-reports/graphs/contributors
.. |GitHub last commit (branch)| image:: https://img.shields.io/github/last-commit/eendroroy/git-reports/master.svg
   :target: https://github.com/eendroroy/git-reports
.. |license| image:: https://img.shields.io/github/license/eendroroy/git-reports.svg
   :target: https://github.com/eendroroy/git-reports/blob/master/LICENSE
.. |GitHub issues| image:: https://img.shields.io/github/issues/eendroroy/git-reports.svg
   :target: https://github.com/eendroroy/git-reports/issues
.. |GitHub closed issues| image:: https://img.shields.io/github/issues-closed/eendroroy/git-reports.svg
   :target: https://github.com/eendroroy/git-reports/issues?q=is%3Aissue+is%3Aclosed
.. |GitHub pull requests| image:: https://img.shields.io/github/issues-pr/eendroroy/git-reports.svg
   :target: https://github.com/eendroroy/git-reports/pulls
.. |GitHub closed pull requests| image:: https://img.shields.io/github/issues-pr-closed/eendroroy/git-reports.svg
   :target: https://github.com/eendroroy/git-reports/pulls?q=is%3Apr+is%3Aclosed
