import pickle
import socket
import threading

from pyexpat.errors import messages

from constants import *


class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.client_socket = None

    def initiate_client(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at  {self.host}:{self.port}")

            self.handle_client()
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
                    print(f"Received a Message From The Server -  {decoded_data}")
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

    def handle_client(self):
        try:
            while True:
                data = input("Enter data to send to the server: ")
                self.send_data(data)
                received_data = self.receive_data()
        except socket.error as e:
            print("error handling client", e)
            return False





def main():
    client = Client(IP, PORT)
    client.initiate_client()


if __name__ == '__main__':
    main()