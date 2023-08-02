# Added packet loss handling
import socket
# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)  # Set socket timeout to 1 second
# Send ping message to server
client_socket.sendto(b'Ping', ('localhost', 12345))
try:
    # Receive pong message from server
    pong_message, server_address = client_socket.recvfrom(1024)
except socket.timeout:
    print("Packet lost: No reply from server")
