#!/usr/bin/python2.7
import os
import re
import sys

def main():
	for line in sys.stdin: #reads input from standard input one line at a time using for loop
		match = re.match('#', line) #skip lines in file that start with '#'
		fields = line.strip().split(':') #strip white spaces and split into array

		if match or len(fields) != 5: #if the line has a '#' or length of fields does not equal five, then skip(continue)
			continue

		username = fields[0]
		password = fields[1]

		gecos = "%s %s,,," % (fields[3],fields[2])

		groups = fields[4].split(',') #the script extracts the values from the comma-separated groups using the split method

		print "==> Creating account for %s..." % (username) #creates a new user account using adduser command with os.system
		cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

		os.system(cmd) #print cmd
		print "==> Setting the password for %s..." % (username) #sets password for user using passwd command with os.system
		cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

		os.system(cmd) #print cmd
		for group in groups: #loops over the groups specified in the in input and assigns user to groups using adduser
			if group != '-':
				print "==> Assigning %s to the %s group..." % (username,group)
			    	cmd = "/usr/sbin/adduser %s %s" % (username,group)
				os.system(cmd) #print cmd

if __name__ == '__main__':
	main()

