DESCRIPTION:
Allows you to run queries against multiple hosts or SSH onto multiple hosts and pull outputs.

I.E. Pull IP addresses for multiple websites or check system states for multiple hosts.

REQUIREMENTS:
- python on local system
- BASH on local and remote system

FIRST RUN:
1. Locate core.py file
2. Make script executeable:
chmod +x core.py

STANDARD USE:
1. Create a hosts.txt file in the same folder as core.py with a hostname or ip address on each line within the file.
2. Run script:
./core.py
3. Check for outputs in output.txt
