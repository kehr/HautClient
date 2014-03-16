/*************************************************************************
 * @File Name:    lock.h
 * @Author:       kehr
 * @Mail:         kehr163@163.com
 * @Created Time: 2013年12月15日 星期日 10时04分37秒
 * @Copyright:    GPL 2.0 applies
 * @Purpose:      实现文件上锁的头文件               
 *************************************************************************/
#ifndef _LOCK_H
#define _LOCK_H
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <stdio.h>
#endif


#ifndef _LOCK_C
#define _LOCK_C
int lock_set (int fd, int type);
#endif
