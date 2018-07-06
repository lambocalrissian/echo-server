import socket
import sys


def client(msg, log_buffer=sys.stderr):
    server_address = ('127.0.0.1', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    # TODO: connect your socket to the server here.
    sock.connect(server_address)

    # you can use this variable to accumulate the entire message received back
    # from the server
    received_message = b''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        # TODO: send your message to the server here.
        sock.sendall(msg.encode('utf-8'))

        # TODO: the server should be sending you back your message as a series
        #       of 16-byte chunks. Accumulate the chunks you get to build the
        #       entire reply from the server. Make sure that you have received
        #       the entire message and then you can break the loop.
        #
        #       Log each chunk you receive.  Use the print statement below to
        #       do it. This will help in debugging problems

        # Look for the response
        amount_received = 0
        amount_expected = len(msg)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            received_message += data

            print('received "{0}"'.format(data.decode('utf8')), file=log_buffer)
            # print('received {!r}'.format(data))

    finally:
        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.
        print('closing socket', file=log_buffer)

        # TODO: when all is said and done, you should return the entire reply
        # you received from the server as the return value of this function.
        sock.close()
        print('Complete Message "{0}"'.format(received_message.decode('utf8')), file=log_buffer)
        
    return received_message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
