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
				os.system("t13-SFP.py")
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
	print('*------------------------------------------*')
	print('*                                          *')
	print('*    JTs Sending & Fuzzing Packets Tool    *')
	print('*                 CYB 339                  *')
	print('*                                          *')
	print('*------------------------------------------*')
	print(' ')
	while True:
		time.sleep(1)
		print(' ')
		print('Choose Target IP Address - Please Enter Valid Target IP: ')
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
	print(' ')
	print("####################\nSending Packets\n ")
	time.sleep(1)
	print(" \n Sending 1 Packet...")
	time.sleep(1)
	send(IP(dst=usrIP)/ICMP())
	time.sleep(1)
	print("----\n ")
	time.sleep(1)
	print(" \n Sending 4 Packets... \n ")
	time.sleep(1)
	sendp(Ether()/IP(dst=usrIP,ttl=(1,4)), iface=tarinface)
	print("----\n ")
	time.sleep(1)
	print(" \n Sending 200 Packets Using .pcap File... \n ")
	time.sleep(1)
	sendp(rdpcap("/home/j/scapy/test/pcaps/pfcp.pcap"))
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nSending Packets Complete!\n')
	time.sleep(1)
	
	print(" \n####################\nFuzzing - Use 'Ctrl + C' to Stop Script! \n ")
	time.sleep(1)
	print(" \n Sending Packets Untill User Stops Attack... \n ")
	time.sleep(1)
	send(IP(dst=usrIP)/fuzz(UDP()/NTP(version=4)),loop=1)
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nFuzzing Packets Complete!\n')
	time.sleep(1)
	restart()
	quit()

if __name__ == '__main__':
	main()



