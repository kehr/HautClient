#!/usr/bin/expect
#������ĵ�ǰ�û����� 
set PassWord 666666
#��ȡ�����д��ݵĽ�����
set PROCESSNAME [lindex $argv 0]

spawn sudo pkill $PROCESSNAME
send "$PassWord\r"
interact
