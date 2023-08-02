# Client Ping Program

This is a simple client ping program in Python that sends a ping message to a server, receives a corresponding pong message back from the server, and determines the delay between when the client sent the ping message and received the pong message. This delay is called the Round Trip Time (RTT).

The functionality provided by the client and server is similar to the functionality provided by standard ping program available in modern operating systems. However, standard ping programs use the Internet Control Message Protocol (ICMP), whereas this program uses a nonstandard (but simple!) UDP-based protocol.

## Requirements

-   Python 3.x
-   Socket module

## Usage

To use this program, simply run the main.py file using Python. The program will send 10 ping messages to the target server over UDP. For each message, the client will determine and print the RTT when the corresponding pong message is returned.

Because UDP is an unreliable protocol, a packet sent by the client or server may be lost. For this reason, the client cannot wait indefinitely for a reply to a ping message. The client will wait up to one second for a reply from the server; if no reply is received, the client will assume that the packet was lost and print a message accordingly.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request. We welcome any contributions, including bug fixes, feature enhancements, and documentation improvements.

## License

This program is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This program is inspired by the standard ping program available in modern operating systems. We would like to thank the developers of the original program for their contributions to the field of networking.
