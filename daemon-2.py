import os
import sys

UMASK = 0
WORKDIR = "/"
MAXFD = 1024

if(hasattr(os,"devnull"))L
	REDIRECT_TO = os.devnull
else:
	REDIRECT_TO = "/dev/null"

def createDaemon():

	try:
		pid = os.fork()
	except OSError, e:
		raise Exception, "%s [%d]" % (e.strerror,e.errno)

	if(pid == 0):
		os.setsid()

	try:
		pid = os.fork()
	except OSError, e:
			raise Exception, "%s [%d] " % (e.strerror, e.errorno)

	
