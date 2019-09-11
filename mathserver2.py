import socket
import sys


def is_num(n):
    return n.isdigit()


def is_power(n):
    n = n/2
    if n == 1:
        return True
    elif n == 2:
        return True
    elif n > 2:
        return is_power(n)
    else:
        return False


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
# to listen to all addresses you can use innaddr_
# any but this is an integer that needs to be converted to dotted decimal
# before it is passed into the bnd
# command a shortcut
# is to use and empty string  ' ' instead of doing the conversion
server_address = ('', 10010)
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
            isInt = data.isdigit()
            if isInt:
                print >> sys.stderr, 'sending data back to the client'
                connection.sendall(str(is_power(float(data))))
            else:
                error = 'that is not a number try again '
                connection.sendall(error)
        else:
            print >> sys.stderr, 'no more data from', client_address
            break

finally:
    # Clean up the connection
    connection.close()
