#FTP
#---
#Anon FTP Scan

import ftplib
import FP
import os
import sys
import time
import ipaddress
import re

def restart():
	time.sleep(2)
	print('---')
	y = 'y'
	n = 'n'
	while True:
		try:
			res = input('\n[!] Do you want to Restart or Quit the Program? [y - Restart, n - Quit]: ')
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

def anonLogin(hostname):
	print(' ')
	print('[+] Starting FTP Scanner...')
	time.sleep(2)
	print(' ')
	print('[*] Starting FTP Scan on the Target IP...')
	time.sleep(1)
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'me@your.com')
		print('\n[*] ' + str(hostname) + ' FTP Anonymous Login Succeeded!')
		ftp.quit()
		return True
		time.sleep(1)
		restart()
	except(Exception, e):
		print('\n[-] ' + str(hostname) + ' FTP Anonymous Login Failed!')
		return False
		time.sleep(1)
		restart()

def main():
	print('*------------------------------------------*')
	print('*                                          *')
	print('*             JTs FTP Scanner              *')
	print('*                 CYB 339                  *')
	print('*                                          *')
	print('*------------------------------------------*')
	print(' ')
	print('The target used in testing was a Metasploitable2 Linux VM')
	print(' ')
	time.sleep(1)
	while True:
		print(' ')
		print('Choose Target IP Address - Please Enter Valid Target IP: ')
		host = input('Enter Target IP Address - ex. <0.0.0.0>: ')
		time.sleep(1)
		try:
			ip_address_obj = ipaddress.ip_address(host)
			print(' ')
			print("You Have Entered a Valid IP Address!! :)")
			print('-----')
			time.sleep(1)
			anonLogin(host)
		except:
			print(' ')
			print("You Have Entered an Invalid IP Address!! :(")
			print('-----')
			time.sleep(1)
		else:
			restart()
			break

if __name__ == '__main__':
	main()


