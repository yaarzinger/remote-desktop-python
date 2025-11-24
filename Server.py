import socket
import threading
from constants import *


class MultiClientServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        print(f"[+] Server listening on {host}:{port}")


    def initiate_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(LISTENING_AMOUNT)

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f'[SERVER] + Client connected to server with {addr}')
            if self.handle_client(client_socket, addr) is False:
                break


    def handle_client(self, client_socket , client_addr):
        try:
            while True:
                data = client_socket.recv(CHUNK_SIZE)
                if not data:
                    print(f"[-] Client {client_addr} disconnected")
                    break
                print(f"[{client_addr}] sent : {data.decode()}")
                if data.decode() == "avishay":
                    client_socket.send(b"HOMO!!!!")  # encoded string (b)
                client_socket.send(b"Message received!")   #encoded string (b)
            return False
        except Exception as e:
            print(f"[!] Error with {client_addr}: {e}")

        client_socket.close()




def main():
    #input(f"Enter ")
    # thread = threading(target = handle_client , args = client_socket , client_addr)

    server = MultiClientServer(HOST, PORT)
    server.initiate_server()


if __name__ == '__main__':
    main()
