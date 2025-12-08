import pickle
import socket
import threading
from constants import *


class MultiClientServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.connected_clients = {}
        print(f"[+] Server listening on {host}:{port}")


    def initiate_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(LISTENING_AMOUNT)

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f'[SERVER] + Client connected to server with {addr}')
            self.connected_clients[addr] = ["Role not chosen", "Available"]

            thread = threading.Thread(
                target=self.handle_client,
                args=(client_socket, addr),
                daemon=True
            )
            thread.start()
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
                if data.decode() == "start":
                    self.handle_user_role_choice(client_socket, client_addr)  # encoded string (b)
                client_socket.send(b"Message received!")   #encoded string (b)
            return False
        except Exception as e:
            print(f"[!] Error with {client_addr}: {e}")

        client_socket.close()
        return None

    def handle_user_role_choice(self, client_socket, client_addr):
        print("Client Started Screen Sharing System. Needs to Choose a role")
        client_socket.send(b"Please send your chosen Role (Sender/Viewer)")
        role = client_socket.recv(CHUNK_SIZE).decode().lower()
        self.connected_clients[client_addr] = [role, "Available"]
        if role == "viewer":
            self.viewer_role_system(client_socket, client_addr) ## function to handle a viewer role
        elif role == "sender":
            self.sender_role_system(client_socket, client_addr) ## function to handle a sender role
        else:
            self.role_not_identified(client_socket, client_addr) ## function to handle error case

    def viewer_role_system(self, client_socket, client_addr):
        print(f"client {client_addr} has connected as viewer")

        """
        This function will utilize the viewer role system
        :param client_socket: client socket
        :param client_addr: client addr
        :return:
        """
        sending_data_dict = {}

        for (ip, _id), (role, status) in self.connected_clients.items():
            if role == "sender" and status == "available":
                sending_data_dict[ip] = [role, status]


        dict_data = pickle.dumps(sending_data_dict)
        client_socket.send(dict_data)

    def sender_role_system(self, client_socket, client_addr):
        """
        This function will utilize the sender role system
        :param client_socket: client socket
        :param client_addr: client addr
        :return:
        """
        print("~~~")

    def role_not_identified(self, client_socket, client_addr):
        """
        This function will handle the case when a user inputs a role that doesn't exist's.
        :param client_socket: client's socket
        :param client_addr: client's addr
        :return:
        """
        print("~~~")
def     main():
    #input(f"Enter ")
    # thread = threading(target = handle_client , args = client_socket , client_addr)

    server = MultiClientServer(HOST, PORT)
    server.initiate_server()


if __name__ == '__main__':
    main()
