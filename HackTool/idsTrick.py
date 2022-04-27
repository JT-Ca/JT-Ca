import ipaddress
import os
import sys
import time
import FP
from random import randint
from scapy.all import *

def ddosT(src, dst, iface, count):
	pkt = IP(src=src, dst=dst)/ICMP(type=8, id=678)/Raw(load='1234')
	send(pkt, iface=iface, count=count)
	
	pkt = IP(src=src, dst=dst)/ICMP(type=0)/Raw(load='LEMME MESS WITH YOU!')
	send(pkt, iface=iface, count=count)
	
	pkt = IP(src=src, dst=dst)/UDP(dport=31335)/Raw(load='PING PONG')
	send(pkt, iface=iface, count=count)
	
	pkt = IP(src=src, dst=dst)/ICMP(type=0, id=456)
	send(pkt, iface=iface, count=count)

def expT(src, dst, iface, count):
	pkt = IP(src=src, dst=dst)/UDP(dport=518)/Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
	send(pkt, iface=iface, count=count)
	
	pkt = IP(src=src, dst=dst)/UDP(dport=635)/Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
	send(pkt, iface=iface, count=count)

def scanT(src, dst, iface, count):
	pkt = IP(src=src, dst=dst)/UDP(dport=7)/Raw(load='CYBOP')
	send(pkt)
	
	pkt = IP(src=src, dst=dst)/UDP(dport=10080)/Raw(load='Wockiana')
	send(pkt, iface=iface, count=count)

def validIP(dst):
	while True:
		try:
			dst = ipaddress.ip_address(dst)
			print('-----')
			print(' ')
			print('[+] Valid IP Address!')
			break
		except ValueError:
			print('-----')
			print(' ')
			print('[+] Invalid IP Address: ' + str(dst))
			time.sleep(1)
			print('-----')
			print(' ')
			print('[!] Restarting Program...')
			print(' ')
			print('-----')
			time.sleep(1)
			restart()

def restart():
	y = 'y'
	n = 'n'
	res = input('Do you want to Restart or Quit the Program? [y - Restart, n - Quit]: ')
	while True:
		try:
			if res == n:
				print('-----')
				print(' ')
				print('[!] Shutting Down Program...')
				time.sleep(1)
				print('[!] Returning Home...')
				print('-----')
				print(' ')
				time.sleep(1)
				FP.cTool()
				quit()
			elif res == y:
				print(' ')
				print('[!] Restarting Program...')
				print('-----')
				print(' ')
				main()
			else:
				break
			
		except ValueError:
			print('-----')
			print(' ')
			print('[!] Please Enter Valid Input!')
			print('-----')
			print(' ')
			restart()
		else:
			break

def main():
	print('*------------------------------------------*')
	print('*                                          *')
	print('*             JTs IDS Tricker              *')
	print('*                 CYB 339                  *')
	print('*                                          *')
	print('*------------------------------------------*')
	time.sleep(1)
	print(' ')
	print('The target used in testing was Snort Installed to \nmy Ubuntu 20.04 VM!')
	print(' ')
	print('-----')
	print(' ')
	print('Choose Network Interface - Press Enter Key for Default (ens33): ')
	iface = input('Enter Network Interface - ex. <eth0>: ')
	if iface == '':
		print('[+] Setting Network Interface to "ens33"...')
		time.sleep(1)
		iface = 'ens33'
		print('[*] Network Interface Set to "ens33"!')
	elif iface == None:
		print('[!] Please Specify Network Interface!')
		print('-----')
		time.sleep(1)
		print('[!] Restarting Program...')
		print(' ')
		print('-----')
		print(' ')
		time.sleep(1)
		restart()
	
	print(' ')
	print('-----')
	print(' ')
	print('Choose Source IP Address - Press Enter Key for Random IP: ')	
	src = input('Enter Source IP Address - ex. <0.0.0.0>: ')
	if src == '':
		print('[+] Setting Random Sorce Address...')
		time.sleep(1)
		src = '.'.join([str(randint(1,254)) for x in range(4)])
		print('[*] Random Source Address Set!')
		print('[*] Random Source Address: ' + str(src))
	elif src == None:
		print('[!] Please Specify Sorce Address!')
		print('-----')
		time.sleep(1)
		print('[!] Restarting Program...')
		print(' ')
		print('-----')
		print(' ')
		time.sleep(1)
		restart()
	
	print(' ')
	print('-----')
	print(' ')
	print('Choose Target IP Address - Please Enter Valid Target IP: ')	
	dst = input('Enter Target IP Address - ex. <0.0.0.0>: ')
	if dst == '':
		print('[!] Please Specify Target IP Address: ')
		print('-----')
		time.sleep(1)
		print('[!] Restarting Program...')
		print(' ')
		print('-----')
		print(' ')
		time.sleep(1)
		restart()
	elif dst == None:
		print('[!] Please Enter Target IP Address: ')
		print('-----')
		time.sleep(1)
		print('[!] Restarting Program...')
		print(' ')
		print('-----')
		print(' ')
		time.sleep(1)
		restart()
	else:
		validIP(dst)
	
	print(' ')
	print('-----')
	print(' ')
	print('Choose Count - Enter "0" for Random Number: ')
	count = int(input('Enter Count (#) of Packets to Send - ex. <"#">: '))
	if count == 0 or count == '' or count == ' ':
		print('[+] Setting Random Count Number...')
		count = int(randint(1,10))
		time.sleep(1)
		print('[*] Count Set to ' + str(count) + '!')
		print(' ')
		print('-----')
		print(' ')
	elif count == None:
		print('[!] Please Specify Packet Count Number: ')
		print('-----')
		time.sleep(1)
		print('[!] Restarting Program...')
		print(' ')
		print('-----')
		print(' ')
		time.sleep(1)
		restart()
	
	ddosT(src, dst, iface, count)
	expT(src, dst, iface, count)
	scanT(src, dst, iface, count)
	time.sleep(1)
	print(' ')
	print('-----')
	print(' ')
	print('[+] IDS Trick Complete!!')
	print(' ')
	print('-----')
	print(' ')
	time.sleep(1)
	restart()
	quit()

if __name__ == '__main__':
	main()


