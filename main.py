import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send ping message to server
client_socket.sendto(b'Ping', ('localhost', 12000))
