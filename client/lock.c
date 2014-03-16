/*************************************************************************
 * @File Name:    lock.c
 * @Author:       kehr
 * @Mail:         kehr163@163.com
 * @Created Time: 2013年12月15日 星期日 10时13分07秒
 * @Copyright:    GPL 2.0 applies
 * @Purpose:      实现文件锁的设置               
 *************************************************************************/
#include "lock.h"

int lock_set(int fd, int type)
{
	//定义文件锁
	struct flock lock;

	//初始化文件锁的状态
	lock.l_whence = SEEK_SET;
	lock.l_start  = 0;
	lock.l_len = 0;
	lock.l_type = type;
	lock.l_pid = -1;

	//判断文件是否可以上锁
	//获取文件已上的锁，并将锁的类型存放在lock.l_type中
	fcntl(fd, F_GETLK, &lock);

	//处理不同的锁类型
	if(lock.l_type != F_UNLCK)
	{
		//该文件已有读取锁
		if(lock.l_type == F_RDLCK)
		{
			printf("Read lock already set by pid: %d\n",lock.l_pid);
		}
		//该文件已有写入锁
		if(lock.l_type == F_WRLCK)
		{
			printf("Write lock already set by pid: %d\n",lock.l_pid);
		}
	}

	//由于l_type可能在判断文件上锁时被改动过(如果文件上锁则改变)
	//还原初始的锁类型
	lock.l_type = type;

	//根据不同的锁类型进行阻塞式上锁，或者给文件解锁
	if((fcntl(fd, F_SETLKW, &lock)) < 0)
	{
		printf("lock failed! type=%d\n",lock.l_type);
		return 1;
	}
	//上锁成功则输出相关提示信息
	switch(lock.l_type)
	{
		case F_RDLCK:
		{
			printf("Read lock set by pid: %d\n",getpid());
		}
		break;

		case F_WRLCK:
		{
			printf("Write lock set by pid: %d\n",getpid());
		}
		break;
		
		case F_UNLCK:
		{
			printf("Release lock by pid: %d\n",getpid());
			return 1;
		}
		break;

		default:
		break;
	}//end of switch
	
	return 0;
}
