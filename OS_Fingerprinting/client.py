import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# specify the server's IP address and port
server_address = ('192.168.99.107', 8080)

# connect to the server
client_socket.connect(server_address)

# send a message to the server (not used in this example)
client_socket.send('Hello, server!'.encode())

# receive the response from the server
data = client_socket.recv(1024).decode()

print('Received data:', data)

# close the connection
client_socket.close()