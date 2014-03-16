#! /usr/bin/env python
# -*-coding:utf-8-*-
# Filename:excute.py
import os
import ConfigParser

filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'excute.sh')
user_info_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'info.ini')

info = ConfigParser.ConfigParser()
info.read(user_info_file)
current_user_passwd = info.get('system','current_user_passwd')

try:
	os.execl(filename,"excute.sh",'none','none',current_user_passwd)
except:
 	raise Exception
