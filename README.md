![ShellGen Logo](https://raw.githubusercontent.com/realagentwhite/ShellGen/master/logo.png)

# ShellGen (Shell Generator)

This is a simple script that will generate a specific or all shellcodes for CTFs using the VPN IP address on tun0 (the IPv4).

## INFORMATION

Update has been made from sys library to argparse library.

## Usage

For help:
- `shellgen -h`
- `shellgen --help`

To update:
- `./shellgen.py -u`
- `./shellgen.py --update`

List shells available:
- `shellgen --shells`
- `shellgen -ls`

An example for using:
- `shellgen --lhost 10.10.12.3 --lport 1234 --shell netcat`

## TODO

List of things to do:

- Clean up some code if any junky code was left behind

To request an improvement or new feature:
- Create an [issue](https://github.com/realagentwhite/ShellGen/issues/new) and mark as `enhancement`

For issues:
- Create an [issue](https://github.com/realagentwhite/ShellGen/issues/new) and mark as `bug`
