#!/usr/bin/env python
import subprocess
import os

# User input
bash = raw_input("BASH Command: ")
sshverif = raw_input("SSH to host? ")
if (sshverif.lower() == "yes" or sshverif.lower() == "y"):
    username = raw_input("Username: ")

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
        arr.append(bash)
    else:
        arr = bash.split()
        arr.append(line)

    # Attempt to issue command
    try:
        output = subprocess.check_output(arr)
    except subprocess.CalledProcessError:
        inputfile.close()
        outputfile.close()
        exit()
    else:
        # Write output to outputfile
        outputfile.write("{2}Hostname{2}\n{0}\n{3}Output{3}\n{1}\n".format(line, output, "-"*21, "-"*22))

inputfile.close()
outputfile.close()
