from hideB2 import *
import sys
sys.path.insert(0, '#1')
import FP
from bs4 import BeautifulSoup
import urllib.request
import os
import time
import re

def pLink(url):
	ab = hideB2()
	ab.anonymize()
	p = ab.open(url)
	h = p.read()
	try:
		print(' ')
		print('[+] HREF Links from Regex: ')
		LF = re.compile('href="(.*?)"')
		L = LF.findall(html)
		for link in L:
			print(link)
		
		print(' ')
		print('[+] HREF Link Parse Complete!!')
		print('---')
		time.sleep(1)
	except:
		pass
	try:
		print(' ')
		print('\n[+] HREF Links from BeautifulSoup: ')
		s = BeautifulSoup(h, features="lxml")
		L = s.findAll(name='a')
		for link in L:
			if link.has_attr('href'):
				print(link['href'])
		
		print(' ')
		print('[+] HREF Link Parse Complete!!')
		print('---')
		time.sleep(1)
		restart()
		quit()
	except:
		pass

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
	print('*            JTs HREF Link Parser          *')
	print('*                 CYB 339                  *')
	print('*                                          *')
	print('*------------------------------------------*')
	print(' ')
	url = input('Please Include http:// in URL!' + '\nEnter URL to Parse: ')
	while True:
		try:
			pLink(url)
			quit()
		except:
			break
		
if __name__ == '__main__':
	main()



