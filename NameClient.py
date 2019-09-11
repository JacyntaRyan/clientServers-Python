import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10002)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:

    message = ''

    while message != 'quit':
        # Send data
        message = raw_input('Enter Client name or "quit" to exit: ')

        if message != 'quit':
            print >> sys.stderr, 'sending "%s"' % message
            sock.sendall(message)
            response = sock.recv(1024)
            print 'received: %s' % response

finally:
    print >> sys.stderr, 'closing socket'
    sock.close()
    print 'exiting.'
