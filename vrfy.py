#!/usr/bin/python
import socket
import sys

def main():
	if len(sys.argv) is not 3 or 4:
		print ("Usage: vrfy.py <email> <server> or vrfy.py ~f <file> <server>")
		sys.exit(0)	
		
	# if just a single email address
	if len(sys.argv) is 3:
		email = sys.argv[1]
		ip = sys.argv[2]
		lookUp(email)		
	
	# if a file of email addresses
	if len(sys.argv) is 4:
		with open(sys.argv[2]) as f:
			data = f.readlines()
			for line in data:				
				lookUp(line)	
	
	#
	# checks if email address is valid
	# email address -> void
	#
	def lookUp(email):
		# Create a Socket
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error as err:
			print "socket creation failed with error %s" %(err)
		# Connect to the Server
		s.connect((ip, 25))
		# Receive the result
		banner = s.recv(1024)
		print banner
		s.send('VRFY ' + email + '\r\n') 
		result = s.recv(1024)
		print "%s: %s" % (email, result)
		# Close the socket
		s.close()
		

if __name__ == "__main__":
	main()
	
	# this is a test comment
