# REMOTE TAIL

### As a user of remote tail, you would be able to display logs from a remote server updating in realtime into command-line interface.

### Assuming that: 

1. The logs are written to a file on the server.
2. You don't have control over the process that writes logs to this file.

### Inputs :
1. Input should be IP address of the server and path to the file on the server that the user wants to tail
2. Implement a watch feature in the client which displays the changes to KV as they happen in real-time.

### I have made this in two ways:

1. [AWS as a Server and Local Client.]()

2. [Server in Docker Container(local) and Local Client.]()