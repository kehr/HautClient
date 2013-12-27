#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File Name:    main.py
# @Module:       intserface.MainInterface
# @Author:       kehr
# @Mail:         kehr163@163.com
# @Created Time: 2013年10月8日
# @Version:      0.1
# @Copyright:    GPL 2.0 applies
# @Description:  HautClient GUI 模块，采用python+GTK开发,开发环境VIM
'''
from gi.repository import Gtk  # @UnresolvedImport
import subprocess
import os
import fcntl  


class MainInterface(Gtk.Window):
    
    def __init__(self):
        self.init_main_interface()

    def init_main_interface(self):
        '''
        初始化主界面
        '''
        Gtk.Window.__init__(self, title="联想天工客户端(linux)")
#         设置主窗体大小
        self.set_size_request(700, 225)
#          窗体大小不可变
        self.set_resizable(False)
#         设置窗体位置
#---------------------待完成


#         定义主界面框架
        self.mainBox = Gtk.Box()
        self.logoBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.loginBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.loginBox.set_size_request(300,225)
        self.logoBox.set_size_request(300,225)
        self.mainBox.pack_start(self.logoBox,True,True,0)
        self.mainBox.pack_start(self.loginBox,True,True,0)
        self.add(self.mainBox)
#        主界面左边添加logo图片
#         加载图片
        logo = Gtk.Image()
        logo.set_from_file("/opt/HautClient/image/logo.jpg")
        logo.show()
#         把图片加载到一个Button中
        imageButton = Gtk.Button()
#         imageButton.set_size_request(80, 40)
        imageButton.add(logo)
        
        fixed = Gtk.Fixed()
        fixed.put(imageButton,0,0)
        self.logoBox.add(fixed)
        
#        主界面右边设置---------------------------------

#         使用table规划位置----------
#         添加用户名密码
        userNameLabel = Gtk.Label("用户名:")
        userPasswdLabel = Gtk.Label("密     码:")
        self.userNameEntry = Gtk.Entry()
        self.userPasswdEntry = Gtk.Entry()
        self.userPasswdEntry.set_visibility(False)
       
#         设置保存密码和自动登陆选项
        self.savePasswd = Gtk.CheckButton("保存密码")
        self.autologin = Gtk.CheckButton("自动登陆")

#         显示登陆信息
        showLoginLabel = Gtk.Label("登陆信息:")
        self.loginInfo = Gtk.Label("尚未登陆！请输入用户名和密码～")
#         显示关于作者
        aboutMeLabel = Gtk.Label()
        aboutMeLabel.set_markup("<a href=\"http://blog.csdn.net/kehrwang\" ><small>关于作者</small></a>")
        aboutMeLabel.set_line_wrap(False)

#         设置登陆和注销按钮选项
        connectButton = Gtk.Button("登陆")
        exitButton = Gtk.Button("注销")
        connectButton.connect("clicked",self.on_connect_button_clicked)
        exitButton.connect("clicked",self.on_exit_button_clicked)        
#         用table整理每个控件的位置
        loginTable = Gtk.Table(6,6,True)
        loginTable.attach(userNameLabel,0,1,0,1)
        loginTable.attach(userPasswdLabel,0,1,1,2)
        loginTable.attach(self.userNameEntry,1,5,0,1)
        loginTable.attach(self.userPasswdEntry,1,5,1,2)
        loginTable.attach(self.savePasswd, 1, 3, 2, 3)
        loginTable.attach(self.autologin, 3, 5, 2, 3)
        loginTable.attach(showLoginLabel, 0, 1, 3, 4)
        loginTable.attach(self.loginInfo, 1, 5, 3, 5)
        loginTable.attach(connectButton, 1, 3, 5, 6)
        loginTable.attach(exitButton, 3, 5, 5, 6)
        loginTable.attach(aboutMeLabel, 0, 1, 5, 6)
        
        
        loginTable.set_col_spacing(0,10)
        loginTable.set_col_spacing(2,20)
        loginTable.set_row_spacing(0,10)
        loginTable.set_row_spacing(3,30)
        self.loginBox.add(loginTable)


               
    def get_user_info(self):
        '''
        获取用户名和密码
        '''
        self.username = self.userNameEntry.get_text()
        self.passwd = self.userPasswdEntry.get_text()

        

                
    def on_connect_button_clicked(self,widget):
        self.get_user_info()

        if self.username == "" or self.passwd == "":
            self.show_warning_dialog("用户名或密码不能为空!")
        else:
            self.loginInfo.set_text("后台正在登陆，请稍后...")
            #debug########################################################################
            #self.cmd_login = '../shell/hautstart.sh ' + self.username + ' ' + self.passwd
            ##############################################################################
            self.cmd_login = '/opt/HautClient/shell/hautstart.sh ' + self.username + ' ' + self.passwd
            self.exec_cmd(self.cmd_login)
            #self.show_login_info()




        
    def on_exit_button_clicked(self,widget):
        
        #debug########################################################################
        # self.cmd_logout = '../shell/hautstop.sh'
        ##############################################################################
        self.cmd_logout = '/opt/HautClient/shell/hautstop.sh'
        self.exec_cmd(self.cmd_logout)

        Gtk.main_quit()  
        
        
    def exec_cmd(self,cmd):

        self.p_login = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        #获取外部命令的执行结果
        self.tmp_info = []
        for line in self.p_login.stdout.readlines():
            #登陆信息打印到界面
            self.tmp_info.append(line)
            print "测试结果：", line,
        #显示认证结果
        result = "登陆异常！"
        if len(self.tmp_info) >= 2:
            result = self.tmp_info[-2]
        elif len(self.tmp_info) == 1 :
            result = self.tmp_info[-1]
        else:
            pass
        self.make_dialog(result)   
 
    def show_login_info(self):
        print "open temp file"
        msg = open("../depend/temp","r")
        #msg = open("log","r")
        print msg.readlines()
        for line in msg:
            print line

        msg.close()


    def show_info_dialog(self,msg):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
        Gtk.ButtonsType.OK, "登陆提示")
        dialog.format_secondary_text(msg)
        dialog.run()
        dialog.destroy()

    def show_warning_dialog(self,msg):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,
        Gtk.ButtonsType.OK, "提示")
        dialog.format_secondary_text(msg)
        dialog.run()
        dialog.destroy()   

    def make_dialog(self, info):
        if 'Offline' in info:
            self.loginInfo.set_text("离线！")
            self.show_warning_dialog("你现在处于离线状态！请检查你的网络连接，确定网线是否插入！")

        elif 'PID:' in info:
            self.loginInfo.set_text("登陆成功！")
            self.show_info_dialog("恭喜你！登陆成功！")
        elif 'Already' in info:
            self.show_warning_dialog("后台正在登陆或者已经登陆成功！无须重复登陆！")   
        elif 'PID' in info:
            self.loginInfo.set_text("注销成功！")
            self.show_warning_dialog("确定退出吗？")
        elif 'kill' in info:
            self.show_warning_dialog("注销成功！")
        elif 'NO' in info:
            self.show_warning_dialog("确定注销并退出吗？")
        elif '用户欠费停机' in info:
            self.loginInfo.set_text("用户欠费停机!")
            self.show_warning_dialog("用户欠费停机！又忘了刷网费了吧～")
        elif 'RADIUS' in info:
            self.loginInfo.set_text("哎呀，找不到RADIUS服务器!")
            self.show_warning_dialog("找不到RADIUS服务器!请尝试退出后重新登陆！")
        elif '用户帐号不存在' in info:
            self.loginInfo.set_text("用户帐号不存在!")
            self.show_warning_dialog("用户帐号不存在!请检查你的用户名和密码。")
        else:
            self.loginInfo.set_text(info)
            self.show_info_dialog(info)         
                
mainWindow = MainInterface()
mainWindow.connect("delete-event", Gtk.main_quit)
mainWindow.show_all()
Gtk.main()

