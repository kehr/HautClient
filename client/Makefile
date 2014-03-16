#########################################################################
# @File Name:    Makefile
# @Author:	     kehr
# @Mail:		 kehr163@163.com
# @Created Time: 2013年12月24日 星期二 10时25分40秒
# @Copyright:    GPL 2.0 applies
#########################################################################
# Target:        hautclient zlevoclient  
# Depend on:     zlevoclient.c lock.c lock.h md5.c md5.h libpcap.a     
# Description:   生成两个异名客户端
#########################################################################
CC=gcc
CFLAGS= -Wall -g
OBJ=lock.o md5.o zlevoclient.o
LIBS = ../libpcap-1.0.0/libpcap.a 
.PHONY: all
all: hautclient zlevoclient

hautclient:$(OBJ)
	$(CC) $(OBJ) $(LIBS) -o $@
zlevoclient:$(OBJ)
	$(CC) $(OBJ) $(LIBS) -o $@
md5.o:md5.c md5.h
	$(CC) $(CFLAGS) -c $<
zlevoclient.o:zlevoclient.c
	$(CC) $(CFLAGS) -c $<
lock.o:lock.c lock.h
	$(CC) $(CFLAGS) -c $<
clean:
	$(RM) *.o *.gch hautclient zlevoclient

