import mechanize
import time
import os
import FP
from random import randint

def tProx(url, hideME, uA):
	b = mechanize.Browser(hideME)
	b.addheaders = uA
	b.set_handle_equiv(False)
	b.set_handle_robots(False)
	p = b.open(url)
	sc = p.read()    
	print(sc)

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
	print('*       JTs Raw HTML Webpage Grabber       *')
	print('*                 CYB 339                  *')
	print('*                                          *')
	print('*------------------------------------------*')
	print(' ')
	time.sleep(1)
	url = input('Please Include http:// in URL!' + '\nEnter URL to Grab: ')
	print(' ')
	print('-----')
	time.sleep(1)
	print(' ')
	print('Choose Source IP Address - This is for Spoofing: ')
	print('Press Enter or 0 for Random IP!')
	print(' ')
	
	ip = input('Enter Spoof Address - <0.0.0.0>: ')
	if ip == '' or ip == ' ' or ip == '0' or ip == None:
		print('[+] Setting Random IP Address...')
		ip = '.'.join([str(randint(1,254)) for x in range(4)])
		time.sleep(1)
		print(' ')
		print('[*] Random Source Address Set!')
		print('[*] Random Source Address: ' + str(ip))
		print('-----')
		print(' ')
		time.sleep(1)
	else:
		print('-----')
		print(' ')

	hideME = ('http', ip)
	print('[+]Setting Spoofed User Agent...')
	print(' ')
	print(' ')
	time.sleep(1)
	uA = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0')]
	print('\nNew User Agent: ' + str(uA))
	print('-----')
	print(' ')
	time.sleep(1)
	print('[+] HTML Grab Starting...')
	print(' ')
	tProx(url, hideME, uA)
	time.sleep(1)
	print(' ')
	print('-----')
	print(' ')
	print('[+] HTML Grab Complete!!')
	print(' ')
	print('-----')
	time.sleep(1)
	restart()
	quit()

if __name__ == '__main__':
	main()


