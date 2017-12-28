#!/usr/bin/python

import socket
import sys

def main():
    if len(sys.argv) is not 3 or 4:
        print("Usage: vrfy.py <email> <server> or vrfy.py ~f <file> <server>")
        sys.exit(0)

    # checking a single email address
    if len(sys.argv) is 3:
        email = sys.argv[1]
        ip = sys.argv[2]
        lookUp(email)

    # checking a file of email addresses
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
            print("socket creation failed with error: %s" % err)
            sys.exit(1)
        # Connect to the Server
        try:
            s.connect((ip, 25))
        except socket.error, err:
            print ("socket connection failed with error: %s" % err)
            sys.exit(1)
        # Receive the result
        banner = s.recv(1024)
        print(banner)
        s.send('VRFY ' + email + '\r\n')
        result = s.recv(1024)
        print("%s: %s" % (email, result))
        # Close the socket
        s.close()
        return

if __name__ == "__main__":
    main()
