import socket           # Import socket module

SIZE = 1024
FORMAT = "utf-8"

filename = input("Enter filename: ") # take filename from user

ip = input("Enter IP Address of server: ") # take IP Address from user
host = ip  # IP taken from the user
port = 6677  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

""" Sending the filename to the server. """
client_socket.send(filename.encode(FORMAT))

"""Getting continuous data from server"""
while True:
    msg = client_socket.recv(SIZE).decode(FORMAT)
    print(msg)