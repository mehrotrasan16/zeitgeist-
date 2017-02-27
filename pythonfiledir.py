# match success grep "\.log$"

import os
import subprocess as sb


os.chdir("/var/log")
os.listdir()

ls = sb.Popen(['ls'],shell=False,stdout=sb.PIPE,universal_newlines=True)
listop = []

print("ls output:")
for line in ls.stdout:
	listop.append(line) #appends with \n at the end of every filename therefore theres a cleaning for loop next
	print(line)

ls.wait()
print("--------------- ls op end------------------")
print("Cleaning Output")

for i in range(0,len(listop)):	# to clean the output of \n chars.
	listop[i] = listop[i][:-1]

j=0
target = []
print("Target Files:")
for i in listop:
	if i.endswith(".log\n"):	#target file type
		target.append(i)
		print(i)		#action
		j = j+1

print("--------------- ls op end------------------")

print("Contents of target files")
for i in target:
	fd = open(i,"r+")
	print(fd.filename)
	line = fd.read()
	print(line)
	print("")

