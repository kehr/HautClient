#!/bin/bash
#########################################################################
# @File Name:    start.sh
# @Author:	     kehr
# @Mail:		 kehr163@163.com
# @Created Time: 2013年12月21日 星期六 14时07分16秒
# @Copyright:    GPL 2.0 applies
# @Description:  use to start zlevlclient
#########################################################################
user_name=$1
passwd=$2
#debug#####################################################
#exec sudo ../depend/hautclient -u $user_name -p $passwd -b
###########################################################
exec sudo hautclient -u $user_name -p $passwd -b
