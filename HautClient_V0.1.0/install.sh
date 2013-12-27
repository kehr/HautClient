#!/bin/bash
#########################################################################
# @File Name:    install.sh
# @Author:	     kehr
# @Mail:		 kehr163@163.com
# @Created Time: 2013年12月21日 星期六 22时36分27秒
# @Copyright:    GPL 2.0 applies
# @Description:  HautClient安装                   
###########################################################################
sudo chmod 755 ./gui/* ./shell/* ./HautClient.desktop ./depend/hautclient ./depend/runhc.sh

user=`whoami`
usergroup=$user
sudo chown $user ./* 
sudo chown $user ./gui/* 
sudo chown $user ./shell/*
sudo chown $user ./depend/*
sudo chgrp $usergroup ./*
sudo chgrp $usergroup ./gui/*
sudo chgrp $usergroup ./shell/*
sudo chgrp $usergroup ./depend/*
echo -e '配置文件权限成功！'
sudo cp ./depend/hautclient ./depend/runhc.sh ./depend/zlevoclient /usr/local/bin/
echo -e '网络驱动安装成功！'
echo -e '创建桌面快捷方式...'
cp ./HautClient.desktop ~/Desktop/
sudo cp ./HautClient.desktop /usr/share/applications/
echo -e '将文件安装到/opt目录下...'
sudo mkdir -p /opt/HautClient/gui
sudo mkdir -p /opt/HautClient/image
sudo mkdir -p /opt/HautClient/shell
sudo cp -r ./gui/*   /opt/HautClient/gui/
sudo cp -r ./shell/* /opt/HautClient/shell/
sudo cp -r ./image/* /opt/HautClient/image/
sudo cp -r ./HautClient.desktop /opt/HautClient/
sudo cp -r ./install.sh /opt/HautClient/
sudo cp -r ./uninstall.sh /opt/HautClient/
sudo chmod 755 /opt/HautClient
sudo chmod 755 /opt/HautClient/*
sudo chmod 755 /opt/HautClient/gui/*
sudo chmod 755 /opt/HautClient/shell/*
echo -e 'HautClient 安装成功！'

exit 0
