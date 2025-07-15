import socket

ip = socket.gethostbyname("247ctf.com")
print("IP address of 247ctf.com: ", ip)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is for IPv4, SOCK_STREAM is for TCP

s.connect(("247ctf.com", 80)) # Connect to the server on port 80 (HTTP)
s.sendall(b"HEAD / HTTP/1.1\r\nHost: 247ctf.com\r\n\r\n") # Send a GET request to the server)
print(s.recv(1024).decode()) # Receive the response from the server and decode it to a string
s.close() # Close the socket connection

### Create and bind a socket to a specific port
client = False
server = False
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if server:
    s.bind(("127.0.0.1", port))
    s.listen()
    
    while True:
        connect, addr = s.accept() # Accept a connection from a client
        connect.send(b"You made it to the socket!")
        connect.close()

if client: # Client mode
    s.connect(("127.0.0.1", port))
    print(s.recv(1024))
    s.close()

### Create a port scanner
for port in [22, 80, 139, 443, 445, 8080]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1) # Set a timeout for the socket connection
    result = s.connect_ex(("127.0.0.1", port)) # Connect to the server on the specified port
    if result == 0:
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))
    s.close()
