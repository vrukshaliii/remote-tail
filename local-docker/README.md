# Server in Docker Container[local] and Local Client.

## In this we have AWS as a server where we have the log files that the client wants to see.

### Inputs :
1. Input should be IP address of the server and path to the file on the server that the user wants to tail.
2. Implement a watch feature in the client which displays the changes to KV as they happen in real-time.

### Steps:
1. Run the Dockerfile to create a Docker Image.
```
docker build -t tail:v1 .
```
2. Run the docker container by mounting the volume that contains file which you want to watch logs.
```
docker run -it -p6677:6677 -v <path_to_file>:$HOME/server/ --name <name_of_container> <image>
```
3. Run `client.py`
```
python3 client.py
```
4. Enter the IP and path of file on client side and you will get logs of that file.

 
You can also use my image **vrukshali26/tail:v1**
```
docker pull vrukshali26/tail:v1
```

And then use this image to launch the container.
