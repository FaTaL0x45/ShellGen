class bcolors:
	DARKPURPLE = "\033[1;35m"
	DARKGREEN  = '\033[92m'
	YELLOW     = '\033[93m'
	RED        = '\033[91m'
	ENDC       = "\033[1;m"
	BOLD       = '\033[1m'

	BOLDGREEN = BOLD+DARKGREEN
	BOLDRED   = BOLD + RED

def print_info(message):
    print((bcolors.RED) + ("[*] ") + (bcolors.YELLOW) + (str(message)))

def print_shell(message):
    print((bcolors.DARKGREEN) + ("[*] ") + (bcolors.DARKGREEN) + (str(message)) + (bcolors.ENDC))

def print_error(message):
    print((bcolors.DARKGREEN) + ("[*] ") + (bcolors.RED) + (str(message)) + (bcolors.ENDC))

def print_shell_types(message):
	print((bcolors.RED) + ("[*] ") + (bcolors.RED) + (str(message)) + (bcolors.ENDC))

def print_list_shells(message):
	print((bcolors.RED) + ("[*] ") + (bcolors.YELLOW) + (str(message)) + (bcolors.ENDC))

def print_msfvenom_shells(message):
	print((bcolors.RED) + ("[*] ") + (bcolors.DARKGREEN) + (str(message)) + (bcolors.ENDC))

