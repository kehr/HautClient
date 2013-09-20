#!/usr/bin/expect
#设置你的当前用户密码 
set PassWord 666666
#你的校园网用户名，就是你的学号
#获取命令行传递的参数作为用户名 
set USERNAME [lindex $argv 0]
#设置登陆密码
#获取命令行传递的参数作为密码
set PASSWORD [lindex $argv 1]
spawn sudo zlevoclient -u $USERNAME -p $PASSWORD -b
send "$PassWord\r"
interact
