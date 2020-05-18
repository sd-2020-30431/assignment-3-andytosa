import socket
import pickle
import select
import errno
from Mediator import Mediator
from UserInterface import UserInterface
from State import State

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
#client_socket.setblocking(False)

state = State()
mediator = Mediator()

while True:
    action = input('\nAction: ')
    sv_command, recv_data, valid = mediator.handle((action, state))
    
    if not valid:
        print("Command invalid!!1!")
        continue
    if sv_command is None:
        continue

    client_socket.send(f"{len(sv_command):<{HEADER_LENGTH}}{sv_command}".encode('utf-8'))

    if recv_data:
        size = client_socket.recv(HEADER_LENGTH)
        size = int(size.decode('utf-8'))

        data = client_socket.recv(size)
        data = pickle.loads(data)

        action_handler.handleData(action, data, state)
