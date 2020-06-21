![ShellGen Logo](https://raw.githubusercontent.com/realagentwhite/ShellGen/master/logo.png)

# ShellGen (Shell Generator)

This is a simple script that will generate a specific or all shellcodes for CTFs using the VPN IP address on tun0 (the IPv4).

## INFORMATION

I am changing up the entire main part of the program and going to use the argparser python library.
If at any time I push an update after 0.7 and you start to find issues, let me know ASAP (open an issue for it and post the errors)

## Usage
- `chmod +x shellgen.py`
- `./shellgen.py <LPORT>`
- `./shellgen.py <LHOST> <LPORT>`
- `./shellgen.py <LHOST> <LPORT> <SHELL TYPE>`

There is also a new help menu:
- `./shellgen.py -h`
- `./shellgen.py --help`

To just run the update:
- `./shellgen.py -u`
- `./shellgen.py --update`

List shells available:
- `./shellgen.py --list-shells`
- `./shellgen.py --shells`


You can choose a specifi payload from the list or enter **all** to print out all the shellcodes.

## TODO

List of things to do:

- Clean up some code (I seriously need to clean up the scripts)
- Instead of using the system library, change to argparser

To request an improvement or new feature:
- Create an [issue](https://github.com/realagentwhite/ShellGen/issues/new) and mark as `enhancement`

For issues:
- Create an [issue](https://github.com/realagentwhite/ShellGen/issues/new) and mark as `bug`
