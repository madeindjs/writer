Writter
=======

A simply class used to normalize all input/output in console (like title, sub-title, etc..).

author: Rousseau Alexandre

created: 2016/06/17


## Installing


Writter may be installed using `setuptools`, `distribute`, or `pip`:

    pip install path.py

The latest release is always updated to the [Python Package Index](http://pypi.python.org/pypi/path.py).

You may also always download the source distribution (zip/tarball), extract
it, and run `python setup.py` to install it.



## Development


To install an in-development version, use the Github links to clone or
download a snapshot of the latest code. Alternatively, if you have git
installed, you may be able to use `pip` or `easy_install` to install directly from
the repository:

    pip install git+https://github.com/jaraco/path.py.git

Testing
=======

Tests are continuously run by Travis-CI: |BuildStatus|_

.. |BuildStatus| image:: https://secure.travis-ci.org/jaraco/path.py.png
.. _BuildStatus: http://travis-ci.org/jaraco/path.py

To run the tests, refer to the ``.travis.yml`` file for the steps run on the
Travis-CI hosts.

Releasing
=========

Tagged releases are automatically published to PyPI by Travis-CI, assuming
the Python 3 build passes.
