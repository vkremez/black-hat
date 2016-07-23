import base64
import socket

target_host = "67.80.26.136"
target_port = 8080

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some Base64-encoded data
client.send(base64.b64encode(b"Secret Code is babalbalababalblaba\r\n\r\n"))

# receive data
response = client.recv(4096)

print response