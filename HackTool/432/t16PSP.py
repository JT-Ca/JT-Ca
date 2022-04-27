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
				os.system("t16-PSP.py")
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
	print('*    JTs Protocol Scanner & Pinger Tool    *')
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
	
	time.sleep(1)
	print(' \n####################\nACK Scan\n ')
	time.sleep(1)
	ans, unans = sr(IP(dst=usrIP)/TCP(dport=[80,666],flags="A"))
	for s,r in ans: 
		if s[TCP].dport == r[TCP].sport: 
			print("%d is unfiltered" % s[TCP].dport)
	for s in unans: 
		print("%d is filtered" % s[TCP].dport)
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	
	
	print(' \n####################\nXmas Scan\n ')
	time.sleep(1)
	ans, unans = sr(IP(dst=usrIP)/TCP(dport=666,flags="FPU") )
	time.sleep(1)
	print(" \n----\n \n Displaying Answered & Unanswered Packet Information...\n ")
	time.sleep(1)
	print(ans, unans)
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	
	print(' \n####################\nARP Ping\n ')
	time.sleep(1)
	ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=usrIP+"/20"),timeout=2)
	time.sleep(1)
	print(" \n----\n \n Displaying Answered & Unanswered Packet Information...\n ")
	time.sleep(1)
	print(ans, unans)
	time.sleep(1)
	print(" \n----\n \nDisplaying Summary of Answer Packets...\n ")
	time.sleep(1)
	print(ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%") ))
	time.sleep(1)
	print(" \n----\n \nArping Target IP...\n ")
	time.sleep(1)
	arping(usrIP)
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	
	print(' \n####################\nICMP Ping\n ')
	time.sleep(1)
	ans, unans = sr(IP(dst=usrIP)/ICMP())
	time.sleep(1)
	print(" \n----\n \n Displaying Answered & Unanswered Packet Information...\n ")
	time.sleep(1)
	print(ans, unans)
	time.sleep(1)
	print(" \n----\n \nDisplaying Summary of Answer Packets...\n ")
	time.sleep(1)
	print(ans.summary(lambda s,r: r.sprintf("%IP.src% is alive") ))
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	
	print(' \n####################\nUDP Ping\n ')
	time.sleep(1)
	ans, unans = sr( IP(dst=usrIP)/UDP(dport=0) )
	time.sleep(1)
	print(" \n----\n \n Displaying Answered & Unanswered Packet Information...\n ")
	time.sleep(1)
	print(ans, unans)
	time.sleep(1)
	print(" \n----\n \nDisplaying Summary of Answer Packets...\n ")
	time.sleep(1)
	print(ans.summary( lambda s,r : r.sprintf("%IP.src% is alive") ))
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	
	print(' \n####################\nTCP Ping\n ')
	time.sleep(1)
	ans, unans = sr( IP(dst=usrIP)/TCP(dport=80,flags="S") )
	time.sleep(1)
	print(" \n----\n \n Displaying Answered & Unanswered Packet Information...\n ")
	time.sleep(1)
	print(ans, unans)
	time.sleep(1)
	print(" \n----\n \nDisplaying Summary of Answer Packets...\n ")
	time.sleep(1)
	print(ans.summary( lambda s,r : r.sprintf("%IP.src% is alive") ))
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	
	print(' \n####################\nTCP Port Scanning\n ')
	time.sleep(1)
	res, unans = sr( IP(dst=usrIP)/TCP(flags="S", dport=(1,150)) )
	time.sleep(1)
	print(" \n----\n \n Displaying Answered & Unanswered Packet Information...\n ")
	time.sleep(1)
	print(res, unans)
	time.sleep(1)
	print(" \n----\n \nDisplaying Summary of Packets...\n ")
	time.sleep(1)
	print(res.nsummary( lfilter=lambda s,r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)) ))
	time.sleep(1)
	print(" \n----\n \nDone.\n ")
	time.sleep(1)
	print(' \n-----\nPings & Scans Complete!\n ')
	time.sleep(1)
	restart()
	quit()

if __name__ == '__main__':
	main()



