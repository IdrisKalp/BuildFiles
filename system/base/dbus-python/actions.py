#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build-python")
    autotools.autoreconf("-fi")

    shelltools.cd("build-python")
    shelltools.system("../configure --prefix=/usr \
                       --localstatedir=/var \
                       --disable-api-docs \
                       --disable-html-docs \
                       --disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    shelltools.cd("build-python")
    autotools.make()

def check():
    pass

def install():
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")

    shelltools.cd("build-python")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
