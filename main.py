# Implemented RTT calculation
import socket
import time
try:
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.settimeout(1)  # Set socket timeout to 1 second
        # Send ping message to server
        start_time = time.time()
        client_socket.sendto(b'Ping', ('localhost', 12345))
        try:
            # Receive pong message from server
            pong_message, server_address = client_socket.recvfrom(1024)
            end_time = time.time()
            rtt = end_time - start_time
            print(f"Received pong message from server. RTT: {rtt} seconds")
        except socket.timeout:
            print("Packet lost: No reply from server")
except socket.error as e:
    print(f"Socket error occurred: {e}")
