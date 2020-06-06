![ShellGen Logo](https://raw.githubusercontent.com/realagentwhite/ShellGen/master/logo.png)

# ShellGen (Shell Generator)

This is a simple script that will generate a specific or all shellcodes for CTFs using the VPN IP address on tun0 (the IPv4).

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

- Clean up some code (if possible without ruining the program)


To request an improvement or new feature:
- Create an [issue](https://github.com/realagentwhite/ShellGen/issues/new) and mark as `enhancement`

For issues:
- Create an [issue](https://github.com/realagentwhite/ShellGen/issues/new) and mark as `bug`
