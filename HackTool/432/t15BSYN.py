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
				os.system("t15-BI-SYNS.py")
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
	print('*    JTs Byte Injector & SYN Scan Tool     *')
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
	print(" \n####################\nInjecting Bytes\n ")
	time.sleep(1)
	print(" \n----\nInjecting Message 'Coming for u! :D' in Packet...\n ")
	time.sleep(1)
	pkt = IP(len=RawVal(b"Coming for u! :D"), src=sourc)
	time.sleep(1)
	print(" \n----\n \nPrinting Packet Information...\n ")
	time.sleep(1)
	print(bytes(pkt))
	time.sleep(1)
	print(" \n----\n ")
	print(pkt)
	time.sleep(1)
	print(" \n----\n ")
	a = pkt.show(dump=True)
	print(a)
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
	print(' \n-----\nPacket Injection Complete!\n ')
	time.sleep(1)

	print(" \n----\n \nDone.\n \n####################\nSYN Scan\n ")
	time.sleep(1)
	print(' \nInitializing SYN Scan on Port 80...\n----\n ')
	p1 = sr1(IP(dst=usrIP)/TCP(dport=80,flags="S"))
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
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \nInitializing SYN Scan on Ports 440, 443, & 666...\n----\n ')
	ans, unans = sr(IP(dst=usrIP)/TCP(sport=666,dport=(440,443),flags="S"))
	time.sleep(1)
	print(" \n----\n \n Displaying Answered & Unanswered Packet Information...\n ")
	print(ans, unans)
	time.sleep(1)
	print(" \n----\n \nDisplaying Stimulus/Response Pairs for Answered Probes...\n ")
	print(ans.summary())
	time.sleep(1)
	print(" \n----\n \nDisplaying TCP Flags for Target Ports...\n ")
	print(ans.summary( lambda s,r: r.sprintf("%TCP.sport% \t %TCP.flags%") ))
	time.sleep(1)
	print(" \n----\nAutomating SYN Scan for Result Collection...\n ")
	time.sleep(1)
	print(" \nTargeting Ports 440 - 443...\n ")
	time.sleep(1)
	print(" \nProducing LaTeX Output...\n ")
	q = report_ports(usrIP,(440,443))
	time.sleep(1)
	print(" \n----\n \nPrinting Packet Information...\n ")
	time.sleep(1)
	print(q)
	time.sleep(1)
	print(" \n----\n \nPrinting Hex & Binary Packet Information...\n ")
	time.sleep(1)
	print(" \n----\n \nHex\n ")
	print(hexdump(q))
	time.sleep(1)
	print(" \n----\n \nBase64\n ")
	time.sleep(1)
	print(export_object(q))
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nSYN Scan Complete!\n ')
	time.sleep(1)
	restart()
	quit()

if __name__ == '__main__':
	main()



