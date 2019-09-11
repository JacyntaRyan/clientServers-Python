import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10010)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:

    message = ''
    numbers_sent = 0
    while message != 'quit' and numbers_sent < 4:
        # Send data
        message = raw_input('Client! Please enter number')
        isNum = message.isdigit()
        if isNum:
            if message != 'quit':
                numbers_sent += 1
                sock.sendall(message)
                print sock.recv(1024)
        else:
            if message != 'quit':
                sock.sendall(message)
                print sock.recv(1024)


finally:
    print >> sys.stderr, 'closing socket'
    sock.close()
    print 'exiting.'
