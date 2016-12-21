#!/usr/bin/env python
from subprocess import call, check_output
import os

# User input
bash = raw_input("BASH Command: ")
sshverif = raw_input("SSH to host? ")
if (sshverif.lower() == "yes" or sshverif.lower() == "y"):
    # BASH command parameter for remote output
    username = raw_input("Username: ")
    command = bash + " 2>&1"
    # command = '{0}'.format(bash + " 2>&1")

# Check if previous outputfile exists, remove if it does
if os.path.isfile('output.txt'):
    os.remove('output.txt')

# Load file to memory and make it read and writeable
inputfile = open('hosts.txt', 'r')
outputfile = open('output.txt', 'w+')

# Loop through textdata
for line in inputfile:
    #remove whitespace from line
    line = str(line).rstrip('\n')
    if (sshverif.lower() == "yes" or sshverif.lower() == "y"):
        # remove whitespace from host, append it to ssh string
        ssh = "ssh " + username + "@" + line
        # create array for check_output to use
        arr = ssh.split()
        arr.append(command)
        # print arr
    else:
        arr = bash.split()
        arr.append(line)
        # print arr

    # Run command using line in inputfile
    output = check_output(arr)
    # Write output to outputfile
    outputfile.write("{1}\nHost: {0}\n{1}\n{2}\n".format(line, "_"*50 ,output))

inputfile.close()
outputfile.close()
