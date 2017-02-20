import sys, os
def daemonize (stdin = '/dev/null', stdout = '/dev/null', stderr = '/dev/null'):
	try:
   # Perform first fork.
		pid = os.fork()
		if pid > 0:
			sys.exit(0)	 # Exit first parent.
	except OSError :
		sys.stderr.write("Fork #1 failed: (%d) %sn" % (OSError.errno,OSError.strerror))
		sys.exit(1)
 # Decouple from parent environment.

	os.chdir("/")
	os.umask(0)
	os.setsid( )
 # Perform second fork.	
	try:
		pid = os.fork()
		if pid > 0:
			sys.exit(0)	 # Exit second parent.
	except OSError :
		sys.stderr.write("Fork #2 failed (%d) %sn " % (OSError.errno,OSError.strerror))
		sys.exit(1)
 # The process is now daemonized, redirect standard file descriptors.
	for f in sys.stdout,sys.stderr: f.flush()

	si = file('/dev/null','r')
	so = file('/tmp/op','a+')
	se = file('/dev/err','a+')
	os.dup2(si.fileno(), sys.stdin.fileno())
	os.dup2(so.fileno(), sys.stdout.fileno())
	os.dup2(se.fileno(), sys.stderr.fileno())
	print("DAEmon Daemon Daemon!, Daemon Daemon Daemon!")
#'''One way that a daemon process differs from a normal backgrounded task is that a daemon process disassociates from its calling process and controlling terminal. This recipe outlines the standard procedure for creating a daemon process. This procedure includes forking once, calling setsid to become a session leader, then forking a second time.

#Along the way, it is common to also change directory to / to ensure that the resulting working directory will always exist. It also ensures that the daemon process doesn't tie up the ability of the system to unmount the filesystem that it happens to be in. It is also typical to set its umask to 0 so that its file creation is set to the most permissive.

#After becoming a daemon, this Python example also sets its standard input (stdin), standard output (stdout), and standard error (stderr) to the values the caller specified.'''
#'''Why not just use the ampersand (&) like you showed a few examples back?" If you do that, you're not totally guaranteed that logging out won't kill that process.'''
