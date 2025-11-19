import socket
import threading

from pyexpat.errors import messages

from constants import CHUNK_SIZE


class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.client_socket = None

    def connect(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at  {self.host}:{self.port}")
            return True
        except socket.error as sock_error:
            print(f"socket error on connection - {sock_error}")
            return False


    def send_data(self, data):
        if self.client_socket:
            try:
                self.client_socket.sendall(data.encode())
                print("data sent to server.")
            except socket.error as e:
                print(f"socket error sending data - ", e)
        else:
            print("Not connected to a server.")

    def receive_data(self):

        if self.client_socket:
            try:
                data = self.client_socket.recv(CHUNK_SIZE)
                if data:
                    decoded_data = data.decode()
                    print(f"Received: {decoded_data}")
                    return decoded_data
                else:
                    print("No data received, server might have closed connection.")
                    return None
            except socket.error as e:
                print(f"Receive error: {e}")
            return None
        else:
            print("Not connected to a server.")
            return None