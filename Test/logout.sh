#!/usr/bin/expect
#设置你的当前用户密码 
set PassWord 666666
#获取命令行传递的进程名
set PROCESSNAME [lindex $argv 0]

spawn sudo pkill $PROCESSNAME
send "$PassWord\r"
interact
