.. cadnano installation

Installation
============

Install Python 3.5
------------------

There are many ways to get Python on your system.

- If you prefer the complete "batteries included" option, `Anaconda Python <https://www.continuum.io/downloads>`__ is available for Mac, Windows or Linux.

- If you just want a clean Python install and nothing else, installers from `python.org <https://www.python.org/>`__ work great too.

- On Mac, [homebrew](http://brew.sh/) is another great way to install Python. 

Cadnano will run on Python 3.3, 3.4 and 3.5, but we only support 3.5. We do not support Python 2.X.


Install cadnano
---------------

1. Install `SIP <https://riverbankcomputing.com/software/sip/intro>`__
   and
   `PyQt5 <https://www.riverbankcomputing.com/software/pyqt/intro>`__ as
   the dependencies.

Currently (6/27/2016), ``PyQt5`` v 5.6 there is a bug with
``QGraphicsItem.itemChange`` that prevents us from being able to use the
`wheels on pypi <https://pypi.python.org/pypi/PyQt5/5.6>`__. We've built
our own versions for Windows and Mac OS X for Python 3.5 64 bit that
don't have this problem:

-  `Mac Python 3.5 SIP
   64-bit <https://hu-my.sharepoint.com/personal/nick_conway_wyss_harvard_edu/_layouts/15/guestaccess.aspx?guestaccesstoken=l9ewGX%2bbgyXEsOFJb4ADP7gEICEj6HvulLGmZ8%2fEzfc%3d&docid=00790fc3650cb4bafa45c2689c71acddd>`__
-  `Mac Python 3.5 PyQt5
   64-bit <https://hu-my.sharepoint.com/personal/nick_conway_wyss_harvard_edu/_layouts/15/guestaccess.aspx?guestaccesstoken=4K1bIvG9EwTvTNm5fxpCRxKLafkWpNd45nLs%2fekGpN0%3d&docid=0980b254529b940d3bb026a8006ab2ff2>`__

And install with:

::

        pip install sip-4.16.9-cp35-none-macosx_10_10_x86_64.whl
        pip install PyQt5-5.5.1-cp35-none-macosx_10_10_x86_64.whl

-  `Windows Python 3.5 SIP
   64-bit <https://hu-my.sharepoint.com/personal/nick_conway_wyss_harvard_edu/_layouts/15/guestaccess.aspx?guestaccesstoken=hHzHovkboxbgsl5ZH46X%2f4uSw52mVuRsTSJOONafsis%3d&docid=06d4c2a4776be46f8b0aad84f43c58532>`__
-  `Windows Python 3.5 PyQt5
   64-bit <https://hu-my.sharepoint.com/personal/nick_conway_wyss_harvard_edu/_layouts/15/guestaccess.aspx?guestaccesstoken=ngRHdMEIrmXYJ3W2dOIrs9L68nVLqeslinQHsbwcGCg%3d&docid=08daf362df3b14bf084973d85e4efd662>`__

And install with:

::

        pip install sip-4.18.1-cp35-none-win_amd64.whl
        pip install PyQt5-5.6.1-cp35-none-win_amd64.whl

**Ultimately**, we plan to maintain ``PyQt5`` wheel builds that work on
Linux, Windows and OS X for Python 3.4+ so you can rely on a single
version of Python 3.X. This of course is subject to change, and will
change this notice once the official wheels are rebuilt with the bug
fix.

2. Then clone the cadnano source from github and run:

   ::

       python setup.py install

Once things are stable, we will distribute a cadnano wheel and start
bundling cross platform installers. For now have fun running radnano.

Advanced: Building from scratch
-------------------------------

Should the above not work for you:

1. Let us know
2. The requirements ``PyQt5`` and ``SIP`` are available from Riverbank
   Computing Limited at:

-  `Qt5 <https://www.qt.io/download/>`__
-  `PyQt5
   downloads <http://www.riverbankcomputing.com/software/pyqt/download5>`__
-  `SIP
   downloads <http://www.riverbankcomputing.com/software/sip/download>`__

Windows
~~~~~~~

Instructions to come.

Mac and Linux
~~~~~~~~~~~~~

These instructions can work 10.10 Yosemite and 10.11 El Capitan under
Xcode 7.0.1 and 6.5. It has also been tested on Debian 7.9 Wheezy Please
provide feedback if you have problems running this in issues.

You can run the included ``pyqt5_check.py`` which will grab, build and
install ``Qt5``, ``SIP`` and ``PyQt5`` in your python environment. It is
cleanest using ``virtualenv`` and ``virtualenvwrapper`` creating a
virtualenv with:

::

    mkvirtualenv --always-copy <myvenv>
    python pyqttools/install_pyqt_from_src.py

and then running the script, but you can definitely install in your
system python if you run:

::

    sudo python pyqttools/install_pyqt_from_src.py

This script only builds required parts of ``Qt5`` and ``PyQt5`` in the
interest of time.

Manual installation of ``PyQt5`` is fine too, but you'll need to trouble
shoot on your own

1. Install ``Qt5``. download the `online
   installer <http://www.qt.io/download-open-source/>`__
2. Build sip and PyQt5 against this ``Qt5``

Of course there are many ways to accomplish this feat, but needless to
say OS X and Linux installs of ``PyQt5`` can be painful for some people.
