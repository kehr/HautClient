#!/usr/bin/expect
#������ĵ�ǰ�û����� 
set PassWord 666666
#���У԰���û������������ѧ��
#��ȡ�����д��ݵĲ�����Ϊ�û��� 
set USERNAME [lindex $argv 0]
#���õ�½����
#��ȡ�����д��ݵĲ�����Ϊ����
set PASSWORD [lindex $argv 1]
spawn sudo zlevoclient -u $USERNAME -p $PASSWORD -b
send "$PassWord\r"
interact
