#!usr/bin/env python 3

import socket
import threading


def client_thread(client_socket: socket.socket, clients: socket.socket, usernames: dict):

    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username

    print(f"User {username} is connected")

    for client in clients:
        if client is not client_socket:
            client.sendall(f"\n{username} has joined the chat \n\n".encode())

    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            if message == "!users":
                client_socket.sendall(f"\n[+] list of available users: {', '.join(usernames.values())}\n\n".encode())
                continue

            for client in clients:
                if client is not client_socket:
                    client.sendall(f"{message}\n".encode())

        except:
            break
    
    client_socket.close()
    clients.remove(client_socket)
    del usernames[client_socket]


def server_program():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #TIME WAIT
    server_socket.bind((host, port))
    server_socket.listen()
    
    print(f"\n[!] The server is listening for local connections")

    clients = list()
    usernames = dict()


    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)

        print(f"A new client is connected: {address}")

        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames))
        thread.daemon = True
        thread.start()

    server_socket.close()


if __name__ == '__main__':
    server_program()