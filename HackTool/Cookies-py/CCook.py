import sys
sys.path.insert(0, '#1')
import FP
from hideB import *
import mechanize
from http.cookiejar import CookieJar, DefaultCookiePolicy
import urllib.request
import os
import random
import time

def CCook():
	print('*------------------------------------------*')
	print('*                                          *')
	print('*           JTs Cookie Grabber             *')
	print('*                CYB 339                   *')
	print('*                                          *')
	print('*------------------------------------------*')
	print(' ')
	ab = hideB(proxies=[], user_agents=[('User-agent: ')])
	url = input('Please Include http:// in URL!' + '\nEnter URL to Grab: ')
	print(' ')
	for attempt in range(0, 5):
		ab.anonymize()
		print('---')
		print('[*] Gathering Page: ')
		response = ab.open(url)
		for cookie in ab.cookie_jar:
			print(cookie)
	
	print(' ')
	print('-----')
	print('[+] 5 Cookies Collected!')
	
	main()
	quit()

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
				print(' ')
				print('[!] Returning Home...')
				time.sleep(1)
				print(' ')
				FP.cTool()
				quit()
			elif res == y:
				os.system("CCook.py")
				print('[!] Restarting Program...')
				print(' ')
				CCook()
				quit()
			else:
				break
			
		except ValueError:
			print('[!] Please Enter Valid Input!')
			print(' ')
			print('-----')
			restart()
			quit()
		else:
			break

def main():
	print('[+] Cookie Grab Complete!!')
	print(' ')
	print('-----')
	time.sleep(1)
	restart()
	quit()

if __name__ == '__main__':
	main()


