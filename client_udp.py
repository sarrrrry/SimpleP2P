import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(bytes("Hello, server!", "utf-8"), (socket.gethostname(), 1235))
# s.connect((socket.gethostname(), 1235))
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
msg = s.recv(1024)
print(msg.decode("utf-8"))