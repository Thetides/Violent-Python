import socket
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