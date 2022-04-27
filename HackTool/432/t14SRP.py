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
				os.system("t14-SRP.py")
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
	print('*-------------------------------------------*')
	print('*                                           *')
	print('*       JTs Sending & Reciving Packets      *')
	print('*                Pts. 1 & 2                 *')
	print('*                  CYB-432                  *')
	print('*                                           *')
	print('*-------------------------------------------*')
	print(' ')
	while True:
		time.sleep(1)
		print(' ')
		print('If the target IP is not correct, this program will not work.')
		print('If the target does not or cannot send a reply packet, this will throw errors')
		time.sleep(1)
		print(' ')
		print('Choose Destination IP Address - Please Enter Valid Target IP: ')
		usrIP = input('Enter Destination IP Address - ex. <0.0.0.0>: ')
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
	
	time.sleep(1)
	print(" \n####################\nSend & Receive Packet(s) - Pt.1\n ")
	time.sleep(1)
	print(" \nSending Packets & Awaiting Response... \n----\n ")
	p = sr1(IP(dst=usrIP)/ICMP()/"XXXXXXXXXXX")
	time.sleep(1)
	print(" \n----\n \nPrinting Packet Information...\n ")
	time.sleep(1)
	print(p)
	print(" \n----\n ")
	s = p.show(dump=True)
	time.sleep(1)
	print(s)
	time.sleep(1)
	print(" \n----\n \nPrinting Hex, Raw, & Binary Packet Information...\n ")
	time.sleep(1)
	print(" \n----\n \nHex\n ")
	time.sleep(1)
	print(hexdump(p))
	time.sleep(1)
	print(" \n----\n \nBinary String (Raw)\n ")
	time.sleep(1)
	pkt_raw = raw(p)
	print(pkt_raw)
	time.sleep(1)
	print(" \n----\n \nBase64\n ")
	time.sleep(1)
	print(export_object(p))
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nSend & Receive Pt. 1 Complete!\n ')
	time.sleep(1)
	
	
	print(" \n----\nDone.\n \n####################\nSend & Receive Packet(s) - Pt. 2\n ")
	time.sleep(1)
	print(" \nSending Packets to Google & Awaiting Response...\n ")
	p1 = sr1(IP(dst=usrIP)/UDP()/DNS(rd=1,qd=DNSQR(qname="www.Google.com")))
	time.sleep(1)
	print(" \n----\n \nPrinting Packet Information...\n ")
	time.sleep(1)
	print(p1)
	print(" \n----\n ")
	ss = p1.show(dump=True)
	print(ss)
	time.sleep(1)
	print(" \n----\n \nPrinting Hex, Raw, & Binary Packet Information...\n ")
	time.sleep(1)
	print(" \n----\n \nHex\n ")
	time.sleep(1)
	print(hexdump(p1))
	time.sleep(1)
	print(" \n----\n \nBinary String (Raw)\n ")
	time.sleep(1)
	pkt_raw = raw(p1)
	print(pkt_raw)
	time.sleep(1)
	print(" \n----\n \nBase64\n ")
	time.sleep(1)
	print(export_object(p1))
	
	print(" \n----\nGathering Data on Ports 20, 21, 22, & 23...\n ")
	time.sleep(1)
	an, unan = sr(IP(dst=usrIP)/TCP(dport=[20,21,22,23]))
	time.sleep(1)
	print(" \n----\n \nDisplaying Answer & Unanswer Data...\n ")
	time.sleep(1)
	print(an, unan)
	time.sleep(1)
	print(" \n----\n \nDisplaying Summary of Answer Packets...\n ")
	time.sleep(1)
	print(an.summary())
	time.sleep(1)
	print(' \n-----\nSending & Reciving Packets Pt. 2 Complete!\n ')
	time.sleep(1)
	restart()
	quit()

if __name__ == '__main__':
	main()



