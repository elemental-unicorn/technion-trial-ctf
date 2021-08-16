#!/usr/bin/env python3
import socketserver
import threading
from time import sleep
from Crypto.Cipher import AES
from os import urandom
from binascii import b2a_hex
from flag import flag
from art import *

BLOCK_SIZE = 16


class Service(socketserver.BaseRequestHandler):

    def handle(self):
        try:
            self.request.settimeout(120)
            self.send(text2art('DuckyDebugDuck', 'rand'))
            key = urandom(BLOCK_SIZE)
            while 1:
                self.send(b'Enter the message you want to encrypt: ')
                resp = self.receive().encode('utf-8')
                message = resp + flag
                print(message)
                self.send(b2a_hex(self.encrypt(self.padding(message), key)))
        except:
            return 0    

    def padding(self, message):
        length = BLOCK_SIZE - len(message) % BLOCK_SIZE if len(message) % BLOCK_SIZE != 0 else 0 
        return message.ljust(len(message) + length, b'\x00')

    def encrypt(self, message, key):
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(message)

    def send(self, string, newline=True):
        string = string.encode('utf-8') if type(string) is str else string
        string = string + b'\n' if newline else string
        self.request.sendall(string)

    def receive(self, prompt="> "):
        self.send(prompt, newline=False)
        return self.request.recv(4096).strip().decode('utf-8')


class ThreadedService(
    socketserver.ThreadingMixIn,
    socketserver.TCPServer,
    socketserver.DatagramRequestHandler,
):
    pass


def main():

    port = 1337
    host = "0.0.0.0"
    service = Service
    server = ThreadedService((host, port), service)
    server.allow_reuse_address = True

    server_thread = threading.Thread(target=server.serve_forever)

    server_thread.daemon = True
    server_thread.start()

    print("Server started on " + str(server.server_address) + "!")

    while True:
        sleep(10)


if __name__ == "__main__":
    main()
