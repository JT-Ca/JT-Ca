#FTP
#---
#Searching for web pages on FTP server

import ftplib
#import FP
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
				#FP.cTool()
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

def returnDefault(ftp):
	try:
		dirList = ftp.nlst()
	except:
		dirList = []
		print('[-] Could Not List Directory Contents!')
		print('[-] Skipping To Next Target...')
		return
	retList = []
	for fileName in dirList:
		fn = fileName.lower()
		if '.php' in fn or '.htm' in fn or '.asp' in fn:
			print('[+] Found Default Page: ' + fileName)
			retList.append(fileName)
			return retList

def main():
	print('*------------------------------------------*')
	print('*                                          *')
	print('*      JTs FTP Server Webpage Search       *')
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
		try:
			ip_address_obj = ipaddress.ip_address(host)
			print(' ')
			print("You Have Entered a Valid IP Address!! :)")
			print('-----')
			time.sleep(1)
			break
		except:
			print(' ')
			print("You Have Entered an Invalid IP Address!! :(")
			print('-----')
		else:
			restart()
			break
	while True:
		time.sleep(1)
		print(' ')
		print('Use the working Username and Password Found By Tool #11 - FTP Brute Forcer')
		print('to gain access to the FTP Server in this Tool!!')
		print(' ')
		time.sleep(1)
		print('Please Enter Credentials to the FTP Server: ')
		print(' ')
		print('In Testing, The Metasploitable 2 VM FTP Credentials are "postgres/postgres"')
		time.sleep(1)
		userName = input('\nEnter Username: ')
		passWord = input('Enter Password: ')
		break
	
	ftp = ftplib.FTP(host)
	ftp.login(userName, passWord)
	returnDefault(ftp)


if __name__ == '__main__':
	main()


