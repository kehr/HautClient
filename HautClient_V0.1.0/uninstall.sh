#!/bin/bash
#########################################################################
# @File Name:    uninstall.sh
# @Author:	     kehr
# @Mail:		 kehr163@163.com
# @Created Time: 2013年12月22日 星期日 16时24分48秒
# @Copyright:    GPL 2.0 applies
# @Description:  卸载HautClient                   
#########################################################################
echo -e '正在卸载网络模块...'
sudo rm -rf /usr/local/bin/runhc.sh
sudo rm -rf /usr/local/bin/hautclient
echo -e '删除快捷方式...'
sudo rm -rf /usr/share/applications/HautClient.desktop
sudo rm -rf ~/Desktop/HautClient.desktop
echo -e '卸载HautClient...'
sudo rm -rf /opt/HautClient
echo -e 'Hautclient卸载成功！'


