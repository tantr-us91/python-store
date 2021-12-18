# socket client
import socket

HOST = 'localhost'
PORT = 1234

try:
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
    s.connect((HOST,PORT))
    message = s.recv(1024)
    s.close()
    full_message = message.decode('utf-8')
    print(full_message)
except OSError as err:
    print('Error ' + str(err.errno) + ': ' + err.strerror)
    sys.exit()
