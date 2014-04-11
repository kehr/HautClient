#########################################################################
# @File Name:    Makefile
# @Author:	     kehr
# @Mail:		 kehr.china@gmail.com
# @Created Time: Sat 15 Mar 2014 01:19:23 PM CST
# @Copyright:    GPL 2.0 applies
#########################################################################
# Description:        install client to your system  
#########################################################################
MAKE = make
SUBDIRS = libpcap-1.0.0 client
CONFDIRS = extend .
.PHONY: all clean install uninstall

define rmfile
	-$(if test -f $(1),\
		sudo rm -rf $(1),\
	echo "$(1) not exit!")
endef

all:
	@echo "\n******** making in libpcap-1.0.0\n"; 
	@(cd libpcap-1.0.0 && ./configure  && chmod 755 * && $(MAKE) -C . )
	@(echo "\n\n You must have root permission to install libpcap in your system! \n")
	-@(sudo make install)
	@echo "\n******** making in client\n"; 
	@(cd client && chmod 755 * && $(MAKE) -C . )
	@echo  "\nFinished ! " 

clean:
	@for subdir in $(SUBDIRS); \
	do \
		echo "\n******** $$subdir cleaning\n"; \
		( cd $$subdir && $(MAKE) clean ); \
		echo "\nFinished ! "; \
	done

install:
	@echo "configuring file's permission ..."
	@(chmod 755 hautclient.py auto-start.py && \
		cd ./extend && \
		chmod 755 ./* &&\
		cd ..)
	@echo "install hautclient and zlevoclient to /usr/local/bin"
	@$(call rmfile ,/usr/local/bin/hautclient)
	@$(call rmfile ,/usr/local/bin/zlevoclient)
	-@(cd ./client/ &&\
		sudo cp hautclient zlevoclient /usr/local/bin/ &&\
		cd ..)
	@echo "Finished!"

uninstall:
	@echo "uninstall hautclient and zlevoclient ..."
	@echo "remove hautclient and zlevoclient ..."
	@$(call rmfile ,/usr/local/bin/hautclient)
	@$(call rmfile ,/usr/local/bin/zlevoclient)
	@$(call rmfile ,./hautclient-logo.png)
	@echo "remove hautclient.desktop ..."
	@$(call rmfile ,/usr/share/applications/hautclient.desktop )
	@$(call rmfile ,$(HOME)/Desktop/hautclient.desktop)
	@$(call rmfile ,$(HOME)/.config/autostart/hautclient.desktop)
	@echo "Finished!"
