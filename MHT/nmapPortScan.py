import FP
import os
import sys
import time
import nmap
import ipaddress
import re

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
	port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
	port_min = 0
	port_max = 65535
	
	print('*------------------------------------------*')
	print('*                                          *')
	print('*          JTs NMap Port Scanner           *')
	print('*                CYB 339                   *')
	print('*                                          *')
	print('*------------------------------------------*')
	print(' ')
	print('The target used in testing was a Metasploitable2 Linux VM ')
	print(' ')
	while True:
		print(' ')
		print('Choose Target IP Address - Please Enter Valid Target IP: ')
		ip_add_entered = input('Enter Target IP Address - ex. <0.0.0.0>: ')
		try:
			ip_address_obj = ipaddress.ip_address(ip_add_entered)
			print(' ')
			print("You Have Entered a Valid IP Address!! :)")
			print('-----')
			break
		except:
			print(' ')
			print("You Have Entered an Invalid IP Address!! :(")
			print('-----')
	
	
	while True:
		print(' ')
		print('Please Enter the Range of Ports Needed for This Scan In the Format: <int>-<int>')
		print(' ')
		port_range = input("Enter the Port Range: ")
		port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
		print('-----')
		if port_range_valid:
			port_min = int(port_range_valid.group(1))
			port_max = int(port_range_valid.group(2))
			break
	
	print(' ')
	nm = nmap.PortScanner()
	for port in range(port_min, port_max + 1):
		try:
			result = nm.scan(ip_add_entered, str(port))
			port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
			print('---')
			print(f"Port {port} is {port_status}")
			print(' ')
				
		except:
			print(' ')
			print(f"Cannot scan port {port}.")
			print('---')
			restart()
	
	print(' ')
	print('-----')
	print('NMap Port Scan Complete!')
	print(' ')
	time.sleep(1)
	restart()
	quit()

if __name__ == '__main__':
	main()



