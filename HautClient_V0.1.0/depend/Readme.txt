ZLEVOClient v0.2 Readme

编译：
	编译需要libpcap库，一般Linux发行版里面安装libpcap-dev包即可，如ubuntu： sudo apt-get install libpcap-dev
	然后从命令行进入源代码目录，运行make，应该很快就能生成zdclient，当然前提是系统中安装了gcc等编译环境，这里不再累赘。

	MacOS / BSD 用户编译：

    Mac用户首先要安装gcc，需要从http://connect.apple.com/下载安装Xcode Tools，具体请查阅Apple Dev的信息。然后下载libpcap的源代码，http://www.tcpdump.org/release/libpcap-1.0.0.tar.gz，解压后分别运行

    ./configure
    make 
    sudo make install

    最后在本程序的源代码目录运行

    make -f Makefile.bsd

运行：
	运行需要root权限：
	
	sudo ./zlevoclient -u username -p password --background
	
	u、p分别是用户名、密码，--background参数可让程序进入后台运行，具体可./zdclient --help查看

    也可使用权限位设置后，不需要sudo而使用root权限执行程序：

    sudo cp zlevoclient /usr/bin
    sudo chmod 1755 /usr/bin/zlevoclient

    这样以后只需直接运行
    zlevoclient -u username -p password --background

	压缩包内提供了启动脚本zlevo_run.sh，用gedit等编辑软件修改sh文件内的username、password，
	以后运行 ./zlevo_run.sh即可。
	
终止：
	默认方式启动的程序，按Ctrl + C即可正常下线，程序终止；
	如果是以后台方式启动的，可另外使用-l参数运行zlevoclient，当然也需要root权限，便能通知原程序下线并退出了。


Another PT Work. 

项目主页： http://code.google.com/p/zlevoclient/
Blog:    http://apt-blog.co.cc
GMail:   pentie@gmail.com

2009-05-20 于广州大学城
