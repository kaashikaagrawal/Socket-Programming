import socket
import platform

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the server's IP address and port
server_address = ('192.168.99.107', 8080)

# bind the socket to the server's address and port
server_socket.bind(server_address)

# listen for incoming connections
server_socket.listen(1)

print('Waiting for client connection...')

while True:
    # accept connections from clients
    client_socket, client_address = server_socket.accept()
    
    print(f'Got connection from {client_address}')
    
    # receive data from client (not used in this example)
    client_socket.recv(1024)
    
    # get OS information
    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    os_architecture = platform.architecture()[0]
    os_machine = platform.machine()
    os_processor = platform.processor()
    os_node = platform.node()
    
    # format the OS information as a string
    os_info = f"Operating System Name: {os_name}\n" \
              f"Operating System Release: {os_release}\n" \
              f"Operating System Version: {os_version}\n" \
              f"Operating System Architecture: {os_architecture}\n" \
              f"Operating System Machine: {os_machine}\n" \
              f"Operating System Processor: {os_processor}\n" \
              f"Operating System Node: {os_node}"
    
    # send the OS information back to the client
    client_socket.send(os_info.encode())
    
    # close the connection
    client_socket.close()
