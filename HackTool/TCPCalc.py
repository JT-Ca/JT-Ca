import FP
import time
import ipaddress
from scapy.all import *

def calTSN(tgt):
	seqNum = 0
	preNum = 0
	diffSeq = 0
	for x in range(1, 5):
		if preNum != 0:
			preNum = seqNum
		pkt = IP(dst=tgt) / TCP()
		ans = sr1(pkt, verbose=0)
		seqNum = ans.getlayer(TCP).seq
		diffSeq = seqNum - preNum
		print('[+] TCP Seq Difference: ' + str(diffSeq))
		print('---')
	return seqNum + diffSeq
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
	print('*         JTs TCP Packet Calculator        *')
	print('*                 CYB 339                  *')
	print('*                                          *')
	print('*------------------------------------------*')
	time.sleep(1)
	print(' ')
	print(' ')
	print('The target used in testing was a Metasploitable2 Linux VM!')
	print(' ')
	print('Choose Target IP Address - Please Enter Valid Target IP: ')
	tgt = input('Enter Target IP Address - <0.0.0.0>: ')
	print('-----')
	
	seqNum = calTSN(tgt)
	print("[+] Next TCP Sequence Number to ACK is: " + str(seqNum+1))
	print('---')	
	time.sleep(1)
	
	print(' ')
	print('[+] TCP Packet Calculation Complete!')
	print('---')
	print(' ')
	restart()
	quit()

if __name__ == '__main__':
	main()


