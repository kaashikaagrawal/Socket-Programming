import socket
import pandas as pd

# Load the book data from an excel file
book_data = pd.read_excel('book_data.xlsx')

# Specify a list of column names to print
column_names = ['Author', 'Pages', 'Genre','abc']

def main():
    host = '192.168.245.107'  # replace with your server's IP address
    port = 12345       # choose a port number that is not currently in use

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)  # only accept one client connection at a time

    print('Server listening on {}:{}'.format(host, port))

    while True:
        conn, addr = server_socket.accept()
        print('Connected to {}:{}'.format(addr[0], addr[1]))

        # receive book name from client
        data = conn.recv(1024)
        book_name = data.decode('utf-8')

        # search for the book in the excel sheet
        book = book_data[book_data['Book'] == book_name]

        # check if the book is found or not
        if book.empty:
            response = 'Book not found'
            conn.send(response.encode())
        else:
            # extract the specified column attributes from the excel sheet
            attributes = []
            for column_name in column_names:
                attributes.append(book[column_name].values[0])

            # create the response string
            response = 'Details of {}: '.format(book_name)
            for i, attribute in enumerate(attributes):
                if i == len(attributes) - 1:
                    response += '{}: {}'.format(column_names[i], attribute)
                else:
                    response += '{}: {}, '.format(column_names[i], attribute)

            conn.send(response.encode())

        conn.close()

if __name__ == '__main__':
    main()
