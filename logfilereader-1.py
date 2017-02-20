import os

LOGDIR = "/var/log"
os.chdir(LOGDIR)

print(os.listdir("."))
print()
print("OR")
print()
for i in os.listdir("/var/log"):
	print(i)


