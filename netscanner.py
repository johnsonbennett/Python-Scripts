#This script is a port scanner that scans a host given by the user as an argument prompt
#Uses the socket library to make TCP/UDP connections to the specified host and port
#It uses argparse to handle command line arguments with takes the host to be scanned and an optional port file
#which is read and scanned
# The script tries to make a TCP connection and if it fails, it tries to make a UDP connection
# If both fail, it prints the error code
# The user can provide there own set of ports to scan by giving it as the second argument in the command line.
# If no port file is given, then the port.txt file which contain some common ports is used by default.
#Even though it is not explicitly mentioned, a port opened for UDP connection means that those ports are often showed as closed in other prot scanner
import socket
import argparse

parser = argparse.ArgumentParser(description='Scan a host for open ports.')
parser.add_argument('host', type=str, help='The host to scan')
parser.add_argument('-p','--port-file', type=str, help='File containing list of ports to scan', default='port.txt')
args = parser.parse_args()
host = args.host
port_file = args.port_file
p = []
with open(port_file, 'r') as file:
    for line in file:
        p.append(int(line.strip()))

Tcon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Ucon = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = host
for port in p:
    result = Tcon.connect_ex((host,port))
    if result == 0:
        print(f'Host {host}:{port} is open for TCP connection')
    else:
        result = Ucon.connect_ex((host,port))
        if result == 0:
            print(f'Host {host}:{port} is open for UDP connection')
        else:
            print(f'Host{host}:{port} is closed with error code {result}')