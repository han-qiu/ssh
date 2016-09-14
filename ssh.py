#!/usr/bin/env python3
import paramiko
import sys
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for i in range(256):
	flag = False
	try:
		ip = "ip"+str(i)
		ssh.connect(ip,username="username",password="password",timeout=1)
		print(ip)
		flag = True
	except:
		print("\r"+str(i),end="")
	if flag:
		sys.exit(0)
