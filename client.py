import socket

HOST = (socket.gethostname(), 8000)
print(HOST) 

eyecar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
eyecar.connect(HOST)  #connect to the server port
print("Connected to", HOST)

msg = eyecar.recv(1024)
print(msg.decode("UTF-8"))