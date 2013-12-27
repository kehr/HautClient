        #获取外部命令的执行结果
        self.tmp_info = []
        for line in self.p_login.stdout.readlines():
            #登陆信息打印到界面
            self.tmp_info.append(line)
            print "测试结果：", line,
        #显示认证结果
        result = "登陆异常！"
        if len(self.tmp_info) >= 2:
            result = self.tmp_info[-2]
        elif len(self.tmp_info) == 1 :
            result = self.tmp_info[-1]
        else:
            pass
        self.make_dialog(result)  



        print "+++++++++++++" 
        print self.p_login.poll()
        print "+++++++++++++" 
        print self.p_login.returncode

                print self.p_login.returncode
        if self.p_login.returncode == 0 or self.p_login.returncode == 1:


        pid = os.fork()
        if pid > 0:
            self.show_login_info()
            os._exit(1)
        self.show_login_info()
        os.setsid()
        os.umask(0)