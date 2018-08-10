![HautClient认证效果](./view.png)

# 介绍

HautClient，这个项目是我在课余时间编写的 **河南工业大学** 校园网认证客户端的 **Linux** GUI 版本。    

目前在Ubuntu 12.04 12.10 13.04 13.10 版本（32位 和 64位）操作系统上编译安装成功。

用到了两个开源项目：

1. [zlevoclient][1]  
由PT桑开发，实现了一个第三方的supplicant客户端，兼容联想的802.1x协议校园网认证系统，支持在Unix系操作系统下跨平台使用。该项目为命令行版本，在湖南人文科技学院、河南工业大学、吉林大学珠海学院，测试完成。  
我下载并编译了该项目并修改部分源码，增加判断当前网络连接状态功能。
2. [Goagent][2]  
作为我朝程序员，对它应该很熟悉，不再介绍。用 goagent 的时候，发现它完全可以用来包装第一个项目（zlevoclient）写一个GUI版本。于是乎就研究了一下源码，实现了现在这个项目：HautClient。

当然，在此之前我也做过其它的两个版本的实现。第一版，用 python+Tkinter 实现了基本的 UI 界面。第二版，用 python + pyGTK模仿 Windows 下的登陆情况实现完整的UI。现在你看到的是第三版，这个版本没有前两个版本的一些bug，安装成功后和使用 goagent 一样方便。

在这个项目中我主要做的事情是让UI和后台的认证进行交互，解决权限问题。

# 配置

## 说明

> 学弟学妹们可能初次使用ubuntu，许多配置还不熟悉，这里就我遇到的一些情况予以说明。  
1. 下面将要介绍到的配置都需要在联网状态下进行，确保你的无线网络可以使用。   
2. 这只是一个校园网认证客户端，安装完成后还需要在你的 Network Connections（网络连接设置） 中设置IP地址。如果Mac地址绑定，需要修改成对应端口的Mac地址，这种情况在你换用别人的端口时会出现。  
3. 如果你对`apt-get`命令不熟悉，那么 Google 一下它的用法吧。   
4. 如果你对`make`命令不熟悉，那么也请 Google 一下它的用法吧。  
5. 这个软件的源码比较简单，希望你在使用的过程中能够理解它的结构，这对你的学习很有帮助。  
**P.S.**  如果你在配置过程中遇到了麻烦，Google是你最好的选择。我已经在多个同学的电脑，不同的系统版本（Ubuntu12.04 13.04 13.10），不同架构（32位，64位）上按照下面的流程配置成功。软件的依赖包在Ubuntu的软件仓库中都有。所以当你遇到问题时请先思考一下是否自己的操作有误。  

希望这个软件能够解决你的目前的问题，并对你的学习产生帮助！  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;—— kehr 2014-4-7




>

## Ubuntu 

1.配置 python 环境，和 UI 库。如果你已经配置过 GoAgent 则可跳过此步骤  

```bash
sudo apt-get install python-dev python-gevent python-vte python-appindicator

```  

2.配置libpcap编译环境

```bash
sudo apt-get install flex bison
```

3.安装 expect, 使用这个'工具'实现免密码登陆。

```bash
sudo apt-get install expect
```

**4.配置登录信息。修改 `extend` 目录下的 `info.ini` 文件，按照文件中的提示配置你登陆的用户名和密码，还有当前用户的密码。**

## Mac

*正在测试 ...*

没有Mac 环境，环境的配置和代码调试无法进行，现暂停开发。
mac 用户可以参考：http://code.google.com/p/zlevoclient/wiki/DeveloperDocument 进行配置。这是PT的命令行版本，可以使用。


# 安装

在你需要保存 HautClient 的位置，打开终端，输入一下命令：

```bash
git clone https://github.com/kehr/HautClient.git
```
```bash  
cd HautClient/
make
sudo make install
```

安装成功后，执行 `hautclient.py` 文件。双击文件，选择 `run`，即可完成登陆。

如果双击无法执行，则需在`hautclient.py`所在目录打开终端，执行以下命令：

```bash
python hautclient.py
```
完成登陆后，你还可以把客户端添加到开机启动项，每次开机后会自动连接认证。

双击 `auto-start.py` ，选择 `run`，即可完成操作。

或者在终端执行如下命令：

```bash
python auto-start.py
```

# 卸载

在`Hautclient`所在目录打开终端，输入：

```
sudo make uninstall
```


# 测试

安装和配置的过程可能还有问题，希望你能够参与测试。你可以把测试结果以issue的形式提交，或者给我发邮件：<kehr.china@gmail.com>，我会及时给予回复。

如果配置过程出现问题，可以参考[zlevoclient][3] 和 [GoAgent][4] 的配置。

**测试说明:**

程序增加了检测网线是否插入的功能。网线未插入，运行后会在vte终端显示：

```
@ERROR: Network Offline!
@SUGGESTION: Please check the network cable is plugged.
```

测试需要插入网线才能看到认证信息。

只要能在vte终端显示正在认证的消息(如下), 测试即可完成。

```
######## Haut Client version 1.1 #########
Device:     eth0
MAC:        00:24:54:1a:d4:31
IP:         0.0.0.0
########################################
>>Protocol: SEND EAPOL-Start

```

# 感谢

感谢 [zlevoclient][1] 和 [GoAgent][2] 的作者提供了优秀的开源代码以供参考。


[1]: https://code.google.com/p/zlevoclient
[2]: https://code.google.com/p/goagent
[3]:https://code.google.com/p/zlevoclient/wiki/StepByStep_Toturial
[4]: https://code.google.com/p/goagent/wiki/GoAgent_Linux
