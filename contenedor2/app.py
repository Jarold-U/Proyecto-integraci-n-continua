import socket

# Configuración del servidor
HOST = "0.0.0.0"
PORT = 5000

# Crear un socket y escuchar conexiones entrantes
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Contenedor 2 esperando mensajes...")
    conn, addr = s.accept()
    with conn:
        print(f"Conexión desde {addr}")
        data = conn.recv(1024)
        if data:
            print(f"Mensaje recibido: {data.decode()}")
            conn.sendall(b"Hola desde el Contenedor 2")
