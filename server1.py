import socket
import sys


# checks all characters are letters and that the first letter is uppercase
def is_valid(data):
    return data.isalpha() and data[0].upper() == data[0]


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
# to listen to all addresses you can use innaddr_
# any but this is an integer that needs to be converted to dotted decimal
# before it is passed into the bnd
# command a shortcut
# is to use and empty string  ' ' instead of doing the conversion
server_address = ('', 10002)
sock.bind(server_address)
print >>sys.stderr, 'starting up on %s port %s' % server_address


# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()

try:
    print >> sys.stderr, 'connection from', client_address

    while True:
        data = connection.recv(1024)
        print >> sys.stderr, 'received "%s"' % data
        if data:
            print >> sys.stderr, 'sending data back to the client'
            if is_valid(data):
                connection.sendall("Hello " + data)
            else:
                connection.sendall("please enter a name beginning with a capital letter and letters only")
        else:
            print >> sys.stderr, 'no more data from', client_address
            break

finally:
    # Clean up the connection
    connection.close()
