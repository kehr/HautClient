#!/usr/bin/env python
# coding:utf-8

from __future__ import with_statement

__version__ = '0.1'

import sys
import os
import re
import time
import ctypes
import platform

def addto_startup_linux():
    filename = os.path.abspath(__file__)
    dirname = os.path.dirname(filename)    
    scriptname = 'hautclient.py'
    DESKTOP_FILE = '''\
[Desktop Entry]
Type=Application
Categories=Network;
Exec=/usr/bin/env python "%s/%s"
Icon=%s/hautclient-logo.png
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=HautClient
Comment=HautClient Launcher
''' % (dirname , scriptname , dirname)
    for dirname in map(os.path.expanduser, ['~/.config/autostart']):
        if os.path.isdir(dirname):
            filename = os.path.join(dirname, 'hautclient.desktop')
            with open(filename, 'w') as fp:
                fp.write(DESKTOP_FILE)

def addto_startup_osx():
    if os.getuid() != 0:
        print 'please use sudo run this script'
        sys.exit()
    import plistlib
    plist = dict(
            GroupName = 'wheel',
            Label = 'org.hautclient.macos',
            ProgramArguments = list([
                '/usr/bin/python',
                os.path.join(os.path.abspath(os.path.dirname(__file__)), 'hautclient.py')
                ]),
            RunAtLoad = True,
            UserName = 'root',
            WorkingDirectory = os.path.dirname(__file__),
            StandardOutPath = 'var/log/hautclient.log',
            StandardErrorPath = 'var/log/hautclient.log',
            KeepAlive = dict(
                SuccessfulExit = False,
                )
            )
    filename = '/Library/LaunchDaemons/org.hautclient.macos.plist'
    print 'write plist to %s' % filename
    plistlib.writePlist(plist, filename)
    print 'write plist to %s done' % filename
   
   
def addto_startup_unknown():
    print '*** error: Unknown system'

def main():
    addto_startup_funcs = {
            'Darwin'    : addto_startup_osx,
            'Linux'     : addto_startup_linux,
            }
    addto_startup_funcs.get(platform.system(), addto_startup_unknown)()


if __name__ == '__main__':
   try:
       main()
   except KeyboardInterrupt:
       pass
