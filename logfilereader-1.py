import os

LOGDIR = "/var/log"
os.chdir(LOGDIR)

print(os.listdir("."))
print
print("OR")
print
numfile=0
for i in os.listdir("/var/log"):
	print(i)
	numfile = numfile + 1

print("Number of Files is: %d" % numfile)

#TODO find regex mathcing the .log files, the .number files read them and then move on to deciphering them.
for i in os.listdir('/var/log'):
	if i == "*.log":
		print(i)

