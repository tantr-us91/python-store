# socket server
import socket, sys

HOST = 'localhost'
PORT = 1234


try:
    # create an AF_INET (Address Family), STREAM (TCP protocol) socket
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
    print('Socket Created')
    s.bind((HOST,PORT))
    s.listen(0)
    print('Listening on port', PORT)
    conn, addr = s.accept()
    print("Connection Established from", addr)
    conn.send(b'Hello, this is the server!')
    conn.close()
except OSError as err:
    print('Error ' + str(err.errno) + ': ' + err.strerror)
    sys.exit()
finally:
    s.close()
