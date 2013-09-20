#! /usr/bin/env python
# -*-coding:utf-8-*-
# Filename:test.py
import os
import re
import sys
import psutil
import subprocess
from Tkinter import *

def getProcessPID(processName):
    '''
    获取processName的PID
    '''
    allProcess = psutil.get_process_list()
    for process in allProcess:
        strProcess = str(process)
        f = re.compile(processName, re.I)
        if f.search(strProcess):
            #print aa.split('pid=')
            
            return strProcess.split('pid=')[1].split(',')[0]  
    
def login():
#     print '用户名：',userNameInput.get()
#     print '密码：',userPasswdInput.get()
#     os.system('./login.sh')
    #调用外部命令
    cmd = './login.sh ' + userNameInput.get() + ' ' + userPasswdInput.get()
    pLogin = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #获取外部命令的执行结果
    for line in pLogin.stdout.readlines():
        print "测试结果：", line,
    
def logout():
    #获取zlevoclient的PID
    print getProcessPID('zlevoclient')
    #调用外部命令
    cmd = './logout.sh zlevoclient'
    pLogin = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #获取外部命令的执行结果
    for line in pLogin.stdout.readlines():
        print "测试结果：", line,







root = Tk()
root.title("联想天工客户端登陆")
root.minsize(150, 130)
root.maxsize(300, 200)



userNamePrompt = Label(root, text='用户名：')
userNamePrompt.pack()

userNameInput = Entry(root)
userNameInput.pack()
print userNameInput.get()

userPasswdPrompt = Label(root, text='密码：')
userPasswdPrompt.pack()


userPasswdInput = Entry(root, show='*')
userPasswdInput.pack()

connectButton = Button(root, text='登陆', command=login)
connectButton.pack(side=LEFT)

exitButton = Button(root, text='注销', command=logout)
exitButton.pack(side=RIGHT)

root.mainloop()
    
    
