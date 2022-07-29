import socket                   # Import socket module
import subprocess
from subprocess import PIPE, run
import time

SIZE = 1024
FORMAT = "utf-8"

# get the hostname
host = '0.0.0.0'
port = 6677  # initiate port no above 1024


server_socket = socket.socket()  # get instance
# The bind() function takes tuple as argument
server_socket.bind((host, port))  # bind host address and port together

# configure how many client the server can listen simultaneously
server_socket.listen(2)
conn, address = server_socket.accept()  # accept new connection
print("Connection from: " + str(address))

""" Receiving the filename from the client. """
filename = conn.recv(SIZE).decode(FORMAT)
print(filename)

def follow(file, sleep_sec=0.1):
    """ Yield each line from a file as they are written.
    `sleep_sec` is the time to sleep after empty reads. """
    line = ''
    while True:
        tmp = file.readline()
        if tmp is not None:
            line += tmp
            if line.endswith("\n"):
                yield line
                line = ''
        elif sleep_sec:
            time.sleep(sleep_sec)


if __name__ == '__main__':
    with open(filename, 'r') as file:
        for line in follow(file):
            conn.send(line.encode(FORMAT)) # send data to the client