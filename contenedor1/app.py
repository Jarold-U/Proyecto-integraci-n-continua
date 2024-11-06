import socket

# Dirección IP y puerto del contenedor 2
HOST = "contenedor2"
PORT = 5000

# Crear un socket y conectarse al contenedor 2
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hola desde el Contenedor 1")
    data = s.recv(1024)

print(f"Mensaje recibido del Contenedor 2: {data.decode()}")
