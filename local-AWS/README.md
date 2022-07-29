# AWS as a Server and Local Client.

## In this we have AWS as a server where we have the log files that the client wants to see.

### Inputs :
1. Input should be IP address of the server and path to the file on the server that the user wants to tail.
2. Implement a watch feature in the client which displays the changes to KV as they happen in real-time.

### Steps:

1. Launch EC2 Instance.
2. Copy the `server.py` to one of the folder in EC2 Instance.
3. In security group of that instance, add an inbound rule, in which mention the public IP of the local system then only both can connect to each other.
4. Run the `server.py` on server. <br>
    ```
    python3 server.py
    ```
5. On local system, run the `client.py` <br>
    ```
    python3 client.py
    ```
6. Enter the IP and path of file on client side and you will get logs of that file.