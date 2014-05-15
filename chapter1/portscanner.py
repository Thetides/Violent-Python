import socket
import os
import sys

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s=socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return
def checkVulns(banner):
	f = open("vuln_banners.txt",'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print "[+] Server is vulnerable: "+banner.strip('\n')



	if 'FreeFloat FTP Server (Version 1.00)' in banner:
		print '[+] FreeFloat FTP Server is Vulnerable.'
	elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
		print '[+] 3CDaemon FTP Server is Vulnerable.'
	elif 'Ability Server 2.34' in banner:
		print '[+] Ability FTP Server is Vulnerable.'
	elif 'Sami FTP Server 2.0.2' in banner:
		print '[+] Sami FTP Server is Vulnerable.'
	else:
		print '[+] FTP Server is not Vulnerable'
	return
def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print '[-] '+filename+' does not exist.'
			exit(0)
			if not os.access(filename, os.R_OK):
				print '[-] '+ filename + ' access denied.'
				exit(0)
		else:
			print '[-] Usage '+ str(sys.argv[0]) + ' <vuln filename>'
			exit(0)
			portList = [21,22,25,80,110,443]
			for x in range(1,255):
				ip = '192.168.1.'+str(x)
				for port in portList:
					banner = retBanner(ip,port)
					if banner:
						print '[+] '+ ip + ': '+ banner
						checkVulns(banner) 
if __name__ == '__main__':
	main()