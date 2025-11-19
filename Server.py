import socket
import threading
from constants import *


class MultiClientServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(LISTENING_AMOUNT)
        print(f"[+] Server listening on {HOST}:{PORT}")

    def handle_client(self, client_socket , client_addr):
        print(f"[+] New connection from {client_addr}")
        try:
            while True:
                data = client_socket.recv(CHUNK_SIZE)
                if not data:
                    print(f"[-] Client {client_addr} disconnected")
                    break
            print(f"[{client_addr}] sent : {data.decode()}")
            client_socket.send(b"Message received!")   #encoded string (b)

        except Exception as e:
            print(f"[!] Error with {client_addr}: {e}")

        client_socket.close()




def main():
    server =


if __name__ == '__main__':
    main()
