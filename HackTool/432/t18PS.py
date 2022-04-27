import FP
import os
import sys
import time
import ipaddress
import re
import scapy
from scapy.all import *

def restart():
	y = 'y'
	n = 'n'
	while True:
		try:
			res = input('Do you want to Restart or Quit the Program? [y - Restart, n - Quit]: ')
			if res == n:
				print(' ')
				print('[!] Shutting Down Program...')
				time.sleep(1)
				print('[!] Returning Home...')
				print('-----')
				print(' ')
				sys.path.insert(0, 'HackTool')
				import FP
				time.sleep(1)
				FP.cTool()
				quit()
			elif res == y:
				print(' ')
				os.system("t18-PS.py")
				print('[!] Restarting Program...')
				print('-----')
				print(' ')
				time.sleep(1)
				main()
				quit()
			else:
				break
			
		except ValueError:
			print(' ')
			print('[!] Please Enter Valid Input!')
			restart()
		else:
			break

def main():
	print('*---------------------------------------*')
	print('*                                       *')
	print('*           JTs Packet Sniffers         *')
	print('*                 CYB 339               *')
	print('*                                       *')
	print('*---------------------------------------*')
	time.sleep(1)
	print(' \nMust Run Ping Command from Target Device to Host Device')
	print('(The One Running The Hacking Tool)\n ')
	time.sleep(1)
	while True:
		time.sleep(1)
		print(' \nChoose Target IP Address - Please Enter Valid Target IP: ')
		usrIP = input('Enter Target IP Address - ex. <0.0.0.0>: ')
		try:
			ip_add = ipaddress.ip_address(usrIP)
			print(' ')
			print("You Have Entered a Valid IP Address!! :)")
			print('-----')
			break
		except:
			print(' ')
			print("You Have Entered an Invalid IP Address!! :(")
			print('-----')
	while True:
		time.sleep(1)
		print(' ')
		print('Choose Target Interface: ')
		tarinface = input('Enter the Targets Interface: ')
		break
	
	time.sleep(1)
	print(" \n####################\nSniffing Packets #1\n ")
	time.sleep(1)
	print(" \n----\nSniffing 15 Packets...\n ")
	time.sleep(1)
	a = sniff(filter="icmp and host " + usrIP, count=15)
	time.sleep(1)
	print(" \n----\n \nPrinting Sniffed Packet Information...\n ")
	time.sleep(1)
	print(a)
	time.sleep(1)
	print(" \n----\n ")
	print(a.nsummary())
	time.sleep(1)
	print(" \n----\n ")
	print(a[1])
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nSniffing #1 Complete!\n ')
	time.sleep(1)
	
	print(" \n####################\nSniffing Packets #2\n ")
	time.sleep(1)
	print(" \n----\nSniffing 10 Packets...\n ")
	time.sleep(1)
	sniff(iface=tarinface, prn=lambda x: x.summary(), count=10)
	time.sleep(1)
	print(" \n----\n \nSniffing #2 Complete!...\n ")
	time.sleep(1)
	
	print(" \n####################\nSniffing Packets #3\n ")
	time.sleep(1)
	print(" \n----\nSniffing 8 Packets...\n ")
	time.sleep(1)
	sniff(iface=tarinface, prn=lambda x: x.show(), count=8)
	time.sleep(1)
	print(" \n----\n \nSniffing #3 Complete!...\n ")
	time.sleep(1)
	
	print(" \n####################\nSniffing Packets #4\n ")
	time.sleep(1)
	print(" \n----\nSniffing 10 Packets...\n ")
	time.sleep(1)
	pkts = sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"), count=10)
	time.sleep(1)
	print(" \n----\n \nPrinting Sniffed Packet Information...\n ")
	time.sleep(1)
	print(pkts)
	time.sleep(1)
	print(" \n----\n \nSniffing #4 Complete!...\n ")
	time.sleep(1)
	restart()
	quit()

if __name__ == '__main__':
	main()



