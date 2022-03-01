import sys
sys.path.insert(0, '#1')
import FP
import os
import PyPDF3
import time
from PyPDF3 import PdfFileReader


def restart():
	y = 'y'
	n = 'n'
	res = input('Do you want to Restart or Quit the Program? [y - Restart, n - Quit]: ')
	while True:
		try:
			if res == n:
				print(' ')
				print('[!] Shutting Down Program...')
				time.sleep(1)
				print('[!] Returning Home...')
				print(' ')
				sys.path.insert(0, 'FinProj')
				import FP
				time.sleep(1)
				FP.cTool()
				quit()
			elif res == y:
				print(' ')
				time.sleep(1)
				print(' ')
				print('[!] Restarting Program...')
				time.sleep(1)
				print(' ')
				print(' ')
				main()
				quit()
			else:
				break
			
		except ValueError:
			print('[!] Please Enter Valid Input!')
			restart()
			quit()
		else:
			break

def main():
	print('*------------------------------------------*')
	print('*                                          *')
	print('*          JTs PDF Metadata Scan           *')
	print('*                 CYB 339                  *')
	print('*                                          *')
	print('*------------------------------------------*')
	print(' ')
	print('***Make sure PDF is in the FinProj Folder***')
	print(' ')
	print(' ')
	fN = input('Enter File Name - <FileName.pfd>: ')
	time.sleep(1)
	print(' ')
	print('[+] Gathering Data...')
	time.sleep(1)
	if fN == '' or fN == ' ' or fN == None:
		print(' ')
		print('[!] Not a Valid File!!')
		print(' ')
		time.sleep(1)
		restart()
	
	PDF = PdfFileReader(fN, 'rb')
	PDFInfo = PDF.getDocumentInfo()
	print(' ')
	print('[*] PDF Metadata - File Name & Path: ')
	print('---> ' + str(fN) + ' <---')
	print(' ')
	for mItem in PDFInfo:
		print('[+] ' + mItem + ': \n' + PDFInfo[mItem] + '\n --- \n')
	time.sleep(1)
	print('[+] PDF Metadata Collection Complete!!')
	time.sleep(1)
	restart()
	quit()	

if __name__ == '__main__':
     main()

