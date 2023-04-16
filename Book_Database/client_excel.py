import socket

def main():
    host = '192.168.245.107'  # replace with your server's IP address
    port = 12345       # choose the same port number as the server

    client_socket = socket.socket()
    client_socket.connect((host, port))
    book_name=input("Enter book name:")
    client_socket.sendall(book_name.encode('utf-8'))

    # receive a response from the server
    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()

if __name__ == '__main__':
    main()
