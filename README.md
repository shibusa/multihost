# Multihost - Multiple host BASH Query Tool

[![Alt text](https://img.youtube.com/vi/MpfbppLUYtA/maxresdefault.jpg)](https://www.youtube.com/embed/MpfbppLUYtA?rel=0;autohide=1;showinfo=0;color=white;cc_load_policy=1)
*(click image above for video demo)*

BASH query tool written in Python.

multihost is designed to do quick queries across large infrastructures. The tool is used to audit configuration inconsistencies across 100+ UNIX systems in pass. This is the inspiration for the [Bastion](https://github.com/shibusa/bastion) project.

## Requirements
- python on local system
- BASH on local and remote system
- ssh-key authentication of remote systems

## First Run
1. Locate core.py file
2. Make script executable
```
chmod +x core.py
```

## Standard use
1. Create a hosts.txt file in the same folder as core.py with a hostname or ip address on each line within the file.
2. Run script
```
./core.py
```
3. Check for outputs in output.txt
