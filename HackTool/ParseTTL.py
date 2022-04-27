import FP
import time as time_module
import time
from random import randint
from scapy.all import *
from IPy import IP as IPTEST

#Lines that are commetented out cause no output

ttlValues = {}
c = 0

def checkTTL(ipsrc, ttl):
	if IPTEST(ipsrc).iptype() == 'PRIVATE':
		return
	if not ttlValues.has_key(ipsrc):
		pkt = sr1(IP(dst=ipsrc) / ICMP(), retry = 0, timeout = 1, verbose = 0)
		ttlValues[ipsrc] = pkt.ttl
		#count()
	if abs(int(ttl) - int(ttlValues[ipsrc])) > THRESH:
		print('\n[!] Detected Possible Spoofed Packet From: ' + ipsrc)
		print('[!] TTL: ' + ttl + ', Actual TTL: ' + str(ttlValues[ipsrc]))
		#print('Count: ' + str(c))
		

def testTTL(pkt):
	try:
		if pkt.haslayer(IP):
				ipsrc = pkt.getlayer(IP).src
				ttl = str(pkt.ttl)
				checkTTL(ipsrc, ttl)
				#count()
				print('[+] Pkt Received From: '+ipsrc+' with TTL: ' + ttl + '\n[+] Count: ' + str(c))

	except:
		pass

def count():
	while True:
		c += 1
		if c == 100:
			print(' ')
			print('TTL Parsing Complete!')
			print(' ')
			print('---')
			restart()
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
	print('*-----------------------------------------------*')
	print('*                                               *')
	print('*             JTs TTL Packet Parser             *')
	print('*                   CYB 339                     *')
	print('*                                               *')
	print('*-----------------------------------------------*')
	print(' ')
	print('*-----------------------------------------------*')
	print('*                                               *')
	print('* Please Note This Tool is a WORK IN PROGRESS!! *')
	print('*                                               *')
	print('* If you wish to end the program, use Ctrl + Z  *')
	print('*                                               *')
	print('* In order to get output, your defult internet  *')
	print('*            browser must be open               *')
	print('*                                               *')
	print('*-----------------------------------------------*')
	print(' ')
	print('Enter Network Interface or Press Enter Key for Default!')
	conf.iface = input('Please Enter Network Interface: ')
	while True:
		if conf.iface == None or conf.iface == '':
			print('[+] Setting Network Interface to "eth0"...')
			conf.iface = 'eth0'
			print('[*] Network Interface Set to "eth0"!')	
			print('---')
			break
		else:
			break
	
	print(' ')
	print('Please Enter Threshold in the Format <#> - ex. 5')
	print('As well, you can press the Enter key for Random Threshold!')
	THRESH = input('Please Enter Threshold: ')
	while True:
		if THRESH == None or THRESH == '':
			print('Setting Thresh to Random Number...')
			THRESH = count = int(randint(1,10))
			print('[*] Thresh Set to ' + str(THRESH) + '!')
			print('---')
			break
		else:
			break
	
	time.sleep(1)
	print(' ')
	print('Parsing Started!')
	print(' ')
	print('Count Set: ' + str(c))
	print(' ')
	sniff(prn=testTTL, store=0)

if __name__ == '__main__':
   main()



