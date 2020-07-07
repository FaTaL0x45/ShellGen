![ShellGen Logo](https://raw.githubusercontent.com/realagentwhite/ShellGen/master/logo.png)

# ShellGen (Shell Generator)

This is a simple script that will generate a specific or all shellcodes for CTFs using the VPN IP address on tun0 (the IPv4).

## INFORMATION

Update has been made from sys library to argparse library (done in version 0.8)

07/07/2020
If there is any feature you would like to add, you can either let me know or
create it yourself and do a pull request and also be added to the list of contributors.

## Usage

For help:
- `shellgen -h`
- `shellgen --help`

If you want to skip update and just get the reverse shell, add `--no-update` to your commands and it will skip it.

To update:
- `./shellgen.py -u`
- `./shellgen.py --update`

List shells available:
- `shellgen --shells`
- `shellgen -ls`

An example for using:
- `shellgen --lhost 10.10.12.3 --lport 1234 --shell netcat`

To request an improvement or new feature:
- Create an [issue](https://github.com/realagentwhite/ShellGen/issues/new) and mark as `enhancement`

For issues:
- Create an [issue](https://github.com/realagentwhite/ShellGen/issues/new) and mark as `bug`


# TODO

- Add option to encode shells if needed
