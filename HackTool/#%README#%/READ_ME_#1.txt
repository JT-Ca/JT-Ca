
JT's 'Hacking' Tools

Creator
JT

Final Project for College Class

This Tool set has a total of 12 different tools and will have future updates with more tools 
being added, bug fixes, etc. 
This is my FIRST ever hacking tool I have created so it’s not capable of much for now.

Most Tools in this kit are Reconnaissance Tools, while only some have Malicious Capabilities,
however, they are extremely limited as they will not be able to attack anything with high 
security. 

***PLEASE BE RESPONIBLE WITH THIS!! I AM NOT LIABLE FOR ANYTHING THAT MAY HAPPEN AS A RESULT OF IRRISPONABLE USE!***

--------------------------------

Prerequisites:

For my tool to run without many errors or bugs, it is recommended that a few things are installed on to your PC. You will need 
VMWare Workstation version 16.x or higher. Then you will need to download an Ubuntu 20.04 VM and a Metasplotable2 Linux VM. 
The Ubuntu VM will be the main one being used while the Metasploitable2 VM will be used as a target.

VMWare: https://www.vmware.com/
Ubuntu: https://ubuntu.com/download/desktop
Metasploitable: https://sourceforge.net/projects/metasploitable/files/Metasploitable2/
CORE & all dependancies: https://coreemu.github.io/core/
Scapy & all dependancies: https://scapy.readthedocs.io/en/latest/

As well, this whole tool was coded using Python 3 so you must download all needed Python Modules and all their Dependencies!!

Python 3: https://www.python.org/downloads/

--------------------------------

Dependencies for Ubuntu VM:
In order for my hacking tool to really work on the Ubuntu VM, there are many dependencies needed to be installed. These are as follows:
-	Python 3.10.0
-	pip
-	Snort & all its dependencies 
-	Nmap & all its dependencies
-	Mechanize & all its dependencies
-	Scapy & all its dependencies
-	Common Open Research Emulator & all its dependencies

Needed Python 3 Modules:
-	sys
-	os
-	time
-	PyPDF2
-	PdfFileReader from PyPDF2
-	mechanize
-	random
-	randint from random
-	http.cookiejar
-	CookieJar from http.cookiejar
-	DefaultCookiePolicy from http.cookiejar
-	urllib.request
-	re
-	bs4
-	BeautifulSoup from bs4
-	time as time_module
-	scapy[complete]
-	IPy
-	IP as IPTEST from IPy
-	nmap
-	ipaddress
-	Scapy[complete]

***As well ALL DEPENDANCIES for each Python 3 Module!!***

For help installing these visit the following links: 
https://pypi.org/
https://scapy.net/
https://github.com/coreemu/core
https://github.com/python-mechanize/mechanize
https://www.snort.org/
https://nmap.org/

--------------------------------

The Main file in this kit is ‘FP.py’! This is the script to run when starting this tool!
Command to start tool: ‘sudo python3 FP.py’
Each script can be ran individually using the same command as above just replace ‘FP.py’ with the script you want to run. 

--------------------------------

Extra Notes:
-	Targets in testing for Tool #6 – IDS Tricker was Snort on Ubuntu 20.04
-	Targets in testing for Tools #5, 7, & 8 are the Metasploitable 2 VM 
-	To have full experience, use this Hacking Tool in CORE Network Topology Emulation

For an explanation of each tool and directions for how they work see ‘Tools & How To Use.txt’

--------------------------------

References & Other Links:
VMWare Workstation:
https://www.vmware.com/
https://www.vmware.com/products/workstation-pro.html
https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html

Ubuntu 20.04 Focal VM:
https://ubuntu.com/download/desktop

Metasploitable2–Linux VM:
https://sourceforge.net/projects/metasploitable/
https://sourceforge.net/projects/metasploitable/files/Metasploitable2/
-	Alternative to VM
https://linuxhint.com/install_metasploit_ubuntu/
https://blog.eldernode.com/install-and-use-metasploit-on-ubuntu/

Ubuntu VM Dependencies:
https://pypi.org/project/pip/
https://pip.pypa.io/en/stable/
https://kifarunix.com/install-and-configure-snort-3-nids-on-ubuntu-20-04/
https://upcloud.com/community/tutorials/install-snort-ubuntu/
https://snort-org-site.s3.amazonaws.com/production/document_files/files/000/008/108/original/Snort_3_on_Ubuntu_18_and_20.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIXACIED2SPMSC7GA%2F20211023%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211023T224202Z&X-Amz-Expires=172800&X-Amz-SignedHeaders=host&X-Amz-Signature=eaaaf69ee92ba2d4b951d951adb3e27e62505e2b5ac52004da993c7508b4c674
https://nmap.org/
https://linuxhint.com/use-nmap-command-ubuntu/
https://manpages.ubuntu.com/manpages/xenial/man1/nmap.1.html
https://mechanize.readthedocs.io/en/latest/
https://github.com/python-mechanize/mechanize
https://pypi.org/project/mechanize/

Python 3:
https://www.python.org/
https://www.python.org/downloads/

Python 3 Modules:
https://docs.python.org/3/library/sys.html
https://docs.python.org/3/library/os.html
https://docs.python.org/3/library/time.html
https://pythonhosted.org/PyPDF2/
https://mechanize.readthedocs.io/en/latest/
https://docs.python.org/3/library/random.html
https://docs.python.org/3/library/http.cookiejar.html
https://docs.python.org/3/library/urllib.request.html
https://docs.python.org/3/library/re.html
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://scapy.readthedocs.io/en/latest/installation.html
 
Tool #1 – #9:
https://pypi.org/
https://pypi.org/project/dpkt/
https://dpkt.readthedocs.io/en/latest/_modules/examples/print_packets.html
https://jon.oberheide.org/blog/2008/10/15/dpkt-tutorial-2-parsing-a-pcap-file/
https://mechanize.readthedocs.io/en/latest/
https://www.rubydoc.info/gems/mechanize/Mechanize:set_proxy
https://coderedirect.com/questions/215632/pythons-mechanize-proxy-support
https://sectigostore.com/blog/13-vulnerable-websites-web-apps-for-pen-testing-and-research/
https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script
https://pypi.org/project/IPy/
https://www.tutorialspoint.com/python/python_if_else.htm
https://stackoverflow.com/questions/20591385/bad-operand-type-for-unary-str
https://docs.python.org/3/tutorial/errors.html
https://stackoverflow.com/questions/12519554/invalid-syntax-in-except-handler-when-using-comma
https://coderedirect.com/questions/165494/invalid-syntax-in-except-handler-when-using-comma
https://stackoverflow.com/questions/20844347/how-would-i-make-a-custom-error-message-in-python
https://stackoverflow.com/questions/11329917/restart-python-script-from-within-itself
https://stackoverflow.com/questions/855493/referenced-before-assignment-error-in-python
https://careerkarma.com/blog/python-local-variable-referenced-before-assignment/
https://www.delftstack.com/howto/python/python-local-variable-referenced-before-assignment/
http://net-informations.com/python/err/local.htm
https://newbedev.com/how-to-make-a-python-program-automatically-restart-itself
https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
https://codefather.tech/blog/validate-ip-address-python/#:~:text=To%20validate%20an%20IP%20address%20using%20Python%20you%20can%20use,IP%20address%20is%20made%20of.
https://stackoverflow.com/questions/36018401/how-to-make-a-script-automatically-restart-itself
https://www.codegrepper.com/code-examples/python/how+to+reboot+a+python+script
https://stackoverflow.com/questions/19782075/how-to-stop-terminate-a-python-script-from-running/34029481
https://stackoverflow.com/questions/73663/how-to-terminate-a-script
https://www.delftstack.com/howto/python/python-run-another-python-script/
https://stackoverflow.com/questions/45384429/how-to-execute-a-python-script-in-a-different-directory
https://datatofish.com/one-python-script-from-another/
https://www.edureka.co/community/50712/possible-call-one-python-script-from-another-python-script
https://www.codegrepper.com/code-examples/python/import+script+from+another+folder+python
https://newbedev.com/how-to-execute-a-python-script-in-a-different-directory
https://www.geeksforgeeks.org/how-to-run-multiple-python-file-in-a-folder-one-after-another/
https://www.geeksforgeeks.org/python-import-module-from-different-directory/
https://stackoverflow.com/questions/52577047/run-another-python-script-in-different-folder
https://www.geeksforgeeks.org/sys-path-in-python/
https://stackoverflow.com/questions/2333400/what-can-be-the-reasons-of-connection-refused-errors
https://stackoverflow.com/questions/2333400/what-can-be-the-reasons-of-connection-refused-errors/2361762
https://stackoverflow.com/questions/11585377/python-socket-error-errno-111-connection-refused
https://github.com/rgerganov/py-air-control/issues/21
https://resources.infosecinstitute.com/topic/port-scanning-using-scapy/


Targets:
https://sourceforge.net/projects/metasploitable/files/Metasploitable2/
https://twitter.com/
https://www.facebook.com/
https://www.google.com/
https://github.com/coreemu/core

Other:
https://pythontutor.com/visualize.html#mode=edit
https://towardsdatascience.com/top-6-python-libraries-for-visualization-which-one-to-use-fe43381cd658

lolcat:
https://github.com/busyloop/lolcat
https://www.youtube.com/watch?v=8EGDxMgNRs0&ab_channel=AlexLynd



