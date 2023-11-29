import socket
import sys
 
# Crear socket
socketAbierto = socket.socket()
 
# Nombre del equipo (o IP), en blanco para localhost
# para recibir conexiones externas
equipo = input("Introduzca la dirección IP o nombre del equipo (en blanco para localhost): ")
# Puerto de escucha del servidor
puerto = int(input("Introduzca el puerto de escucha: "))
 
try:
    """
    El método bind conecta el socket en una tupla que especifica
    una dirección y un puerto
    """
    socketAbierto.bind((equipo, puerto))
except socket.error as message:
    print("Falló la escucha por el puerto ", puerto)
    print(message)
    sys.exit()
# Iniciamos la escucha
socketAbierto.listen()
print("Escuchando en el puerto: ", puerto)
while True:
    # A la espera de una conexión de un cliente
    connection,address = socketAbierto.accept()
    print("Cliente ", address[0],address[1], " conectado")
    # Enviar un mensaje al cliente conectado
    mensaje = "Mensaje enviado al cliente desde el servidor"
    connection.send(mensaje.encode())
    # Cerrar el socket
    connection.close()