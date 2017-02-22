import os
import sys

"""necessary to disown all child procs and parent procs"""
UMASK = 0
WORKDIR = "/home/sanket"
MAXFD = 1024

'''if(hasattr(os,"devnull")):
	REDIRECT_TO = os.devnull
else:
	REDIRECT_TO = "/dev/null"
'''
def createDaemon():

	try:
		pid = os.fork() #create the process
	except OSError:
		raise  "%s [%d]" % (OSError.strerror,OSError.errno)

	if(pid == 0):
		os.setsid() #(set session id) i.e create new session

		#second child process
		try:
			pid = os.fork()
		except OSError:
				raise  "%s [%d] " % (OSError.strerror, OSError.errorno)
		if(pid == 0):
			os.chdir(WORKDIR)
			os.umask(UMASK)
		else:
			os._exit(0)

	else:
		os._exit(0)

	try:
		maxfd = os.sysconf("SC_OPEN_MAX")
	except( AttributeError,ValueError):
		maxfd = MAXFD

	return(0)
'''
	for fd in range(0,maxfd):
		try:
			os.close(fd)
		except OSError:
			pass

	os.open(REDIRECT_TO,os.O_RDWR) #will return 0, therefore the 0 file desc will point to /dev/null or redirect_to

	os.dup2(0,1)
	os.dup2(0,2)

	return(0)
'''


if __name__ == "__main__":
	retCode = createDaemon()
	os.system("echo 'Here'")
	procParams = """
	   return code = %s
	   process ID = %s
	   parent process ID = %s
	   process group ID = %s
	   session ID = %s
	   user ID = %s
	   effective user ID = %s
	   real group ID = %s
	   effective group ID = %s
	   """ % (retCode, os.getpid(), os.getppid(), os.getpgrp(), os.getsid(0),
	   os.getuid(), os.geteuid(), os.getgid(), os.getegid())

	open("createDaemon.log", "w").write(procParams + "\n")

	sys.exit(retCode)
