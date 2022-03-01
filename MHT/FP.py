#CYB 339 - Final Project 
#Prof. Ish Morales
#JT Cavallaro (jocavall)
#October 13, 2021

#Global Imports
import sys
import os
import time

#Tool 1 - PDF Metadata Collector
import PyPDF3
from PyPDF3 import PdfFileReader

#Tool 2 - HTML Grab
import mechanize
import time
from random import randint

#Tool 3 - Cookie Grab
import mechanize
import http.cookiejar
import random
import urllib.request
import os
import random
from http.cookiejar import CookieJar, DefaultCookiePolicy

#Tool 4 - Link Parser
import urllib.request
import os
import re
from bs4 import BeautifulSoup

#Tool 5 - TTL Pkt Parser
import time as time_module
import time
from random import randint
from scapy.all import *
from IPy import IP as IPTEST

#Tool 6 - Nmap Port Scanner
import os
import sys
import time
import nmap
import ipaddress
import re

#Tool 7 - IDS Tricker
import ipaddress
import os
import sys
import time
from random import randint
from scapy.all import *

#Tool 8 - TCP Calculator
import time
from scapy.all import *

#Tool 9 - SYN Flooder
import ipaddress
import os
import sys
import time
from random import randint
from scapy.all import *

#Tool 10 - Anonymous FTP Scanner
import ftplib
import FP
import os
import sys
import time
import ipaddress
import re

#Tool 11 - Brute Force FTP Credentials


#Tool 12 - FTP Server Webpage Search


def load():
	print('      ___           ___           ___           ___     ')
	print('     /\__\         /\  \         /\  \         /\__\    ')
	print('    /:/  /        /::\  \       /::\  \       /:/  /    ')
	print('   /:/__/        /:/\:\  \     /:/\:\  \     /:/__/     ')
	print('  /::\  \ ___   /::\~\:\  \   /:/  \:\  \   /::\__\____ ')
	print(' /:/\:\  /\__\ /:/\:\ \:\__\ /:/__/ \:\__\ /:/\:::::\__ ')
	print(' \/__\:\/:/  / \/__\:\/:/  / \:\  \  \/__/ \/_|:|~~|~   ')
	print('      \::/  /       \::/  /   \:\  \          |:|  |    ')
	print('      /:/  /        /:/  /     \:\  \         |:|  |    ')
	print('     /:/  /        /:/  /       \:\__\        |:|  |    ')
	print('     \/__/         \/__/         \/__/         \|__|    ')
	print('      ___                       ___           ___           ___       ___     ')
	print('     /\__\          ___        /\  \         /\  \         /\__\     |\__\    ')
	print('    /:/ _/_        /\  \      /::\  \       /::\  \       /:/  /     |:|  |   ')
	print('   /:/ /\__\       \:\  \    /:/\ \  \     /:/\:\  \     /:/  /      |:|  |   ')
	print('  /:/ /:/ _/_      /::\__\  _\:\~\ \  \   /::\~\:\  \   /:/  /       |:|__|__ ')
	print(' /:/_/:/ /\__\  __/:/\/__/ /\ \:\ \ \__\ /:/\:\ \:\__\ /:/__/        /::::\__ ')
	print(' \:\/:/ /:/  / /\/:/  /    \:\ \:\ \/__/ \:\~\:\ \/__/ \:\  \       /:/~~/~   ')
	print('  \::/_/:/  /  \::/__/      \:\ \:\__\    \:\ \:\__\    \:\  \     /:/  /     ')
	print('   \:\/:/  /    \:\__\       \:\/:/  /     \:\ \/__/     \:\  \    \/__/      ')
	print('    \::/  /      \/__/        \::/  /       \:\__\        \:\__\              ')
	print('     \/__/                     \/__/         \/__/         \/__/              ')
	print('                                                                              ')
	print('*-----------------------*')
	print('*                       *')
	print('*    JTs Hacker Tool    *')
	print('*     Hack Wisely!!     *')
	print('*                       *')
	print('*-----------------------*')
	print(' ')
	print(' ')
	time.sleep(1)

def shutdown():
	print(' ')
	z = input('Are you Sure? [y/n]')
	y = 'y'
	n = 'n'
	if z == y:
		print(' ')
		print('Thank you for using my Hacking Tool!')
		print(' ')
		time.sleep(1)
		print('Shutting Down...')
		print('-----')
		print(' ')
		time.sleep(1)
		quit()
	elif z == n:
		print(' ')
		print('Okay!! Returning Home!')
		print('-----')
		print(' ')
		time.sleep(1)
		print('...')
		time.sleep(1)
		print('...')
		time.sleep(1)
		main()
		quit()
	else:
		print(' ')
		print('[!] Your Input is Invalid!')
		print(' ')
		time.sleep(1)
		print('[!] Restarting Shutdown...')
		print('-----')
		print(' ')
		time.sleep(1)
		shutdown()
					
def cTool():
	time.sleep(1)
	print('[!] One Moment Please...')
	print(' ')
	time.sleep(1)
	print('*--------------------------------------*')
	print('* Tool #1 - PDF Metadata Collector     *')
	print('* Tool #2 - Raw HTML Webpage Grabber   *')
	print('* Tool #3 - Cookie Grab                *')
	print('* Tool #4 - HREF Link Parser           *')
	print('* Tool #5 - Nmap Port Scanner          *')
	print('* Tool #6 - IDS Tricker                *')
	print('* Tool #7 - TCP Calculator             *')
	print('* Tool #8 - SYN Flooder                *')
	print('* Tool #9 - TTL Pkt Parser (BUGGY)     *')
	print('* Tool #10 - Anonymous FTP Scanner     *')
	print('* Tool #11 - FTP Brute Force           *')
	print('* Tool #12 - FTP Server Webpage Search *')
	print('*--------------------------------------*')
	print(' ')
	time.sleep(1)
	print(' ')
	print('Please Enter only the number of the tool you wish to use!')
	print('Ex. if you wish to use Tool #2 - HTML Grab, Enter 2')
	print(' ')
	print('As well, you can enter 0 to quit the program.')
	print(' ')
	time.sleep(1)
	tool = int(input('Please Enter Tool Number: '))
	t0 = 0
	t1 = 1
	t2 = 2
	t3 = 3
	t4 = 4
	t5 = 5
	t6 = 6
	t7 = 7
	t8 = 8
	t9 = 9
	t10 = 10
	t11 = 11
	t12 = 12
	
	while True:
		try:
			if tool == 0:
				print(' ')
				print('[!] One Moment Please...')
				print('-----')
				print(' ')
				time.sleep(1)
				shutdown()
				quit()
			if tool == 1:
				print(' ')
				sys.path.insert(0, 'PDF-py')
				import PDFMetadata
				print('[+] Opening PDF Metadata Collector...')
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				PDFMetadata.main()
				quit()
			elif tool == 2:
				print(' ')
				print('[+] Opening HTML Grabber...')
				print(' ')
				import HTMLGrabber
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				HTMLGrabber.main()
			elif tool == 3:
				print(' ')
				sys.path.insert(0, 'Cookies-py')
				import CCook
				print('[+] Opening Cookie Grabber...')
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				CCook.CCook()
				quit()
			elif tool == 4:
				print(' ')
				sys.path.insert(0, 'ParsLink-py')
				import ParL
				print('[+] Opening Link Parser...')
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				ParL.main()
				quit()
			elif tool == 5:
				print(' ')
				print('[+] Opening NMap Port Scanner...')
				import nmapPortScan
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				nmapPortScan.main()
				quit()
			elif tool == 6:
				print(' ')
				print('[+] Opening IDS Tricker...')
				import idsTrick
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				idsTrick.main()
				quit()
			elif tool == 7:
				print(' ')
				print('[+] Opening TCP Packet Calculator...')
				import TCPCalc
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				TCPCalc.main()
				quit()
			elif tool == 8:
				print(' ')
				print('[+] Opening SYN Packet Flooder...')
				import SYNFlood
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				SYNFlood.main()
			elif tool == 9:
				print(' ')
				print('[+] Opening TTL Packet Parser...')
				import ParseTTL
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				ParseTTL.main()
				quit()
			elif tool == 10:
				print(' ')
				print('[+] Opening Anonymous FTP Scanner...')
				import FTPScan
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				FTPScan.main()
				quit()
			elif tool == 11:
				print(' ')
				print('[+] Opening FTP Brute Forcer...')
				import FTPBF
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				FTPBF.main()
				quit()
			elif tool == 12:
				print(' ')
				print('[+] Opening FTP Server Webpage Searcher...')
				import FTPWP
				print(' ')
				time.sleep(0.5)
				print('[!] Please be Responsable!')
				print('-----')
				print(' ')
				time.sleep(1)
				FTPWP.main()
				quit()
			else:
				print('[!] Your Input is Invalid!')
				print(' ')
				time.sleep(1)
				print('[!] Restarting Program...')
				print('-----')
				print(' ')
				time.sleep(1)
				main()
				quit()
		except:
			break

def main():
	load()
	cTool()
	quit()

if __name__ == '__main__':
	main()


