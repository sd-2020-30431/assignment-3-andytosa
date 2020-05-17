import socket
import select
import sqlite3
import pickle

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]
clients = {}

print(f'Listening for connections on {IP}:{PORT}')

connection = sqlite3.connect('a2.db')
cursor = connection.cursor()

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        
        message_length = int(message_header.decode('utf-8'))
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return False


while True:

    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            sockets_list.append(client_socket)
            clients[client_socket] = client_address

            print('Accepted new connection from {}:{}'.format(*client_address))

        else:
            message = receive_message(notified_socket)

            if message is False:
                print('Closed connection from {}'.format(clients[notified_socket]))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f'Received message from {user}: {message["data"].decode("utf-8")}')

            sv_command = message['data'].decode('utf-8')
            cursor.execute(sv_command)
            connection.commit()

            if sv_command[:6] == 'SELECT':
                rows = cursor.fetchall()
                data = pickle.dumps(rows)
                notified_socket.send(f'{len(data):<{HEADER_LENGTH}}'.encode('utf-8') + data)


    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
