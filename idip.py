import socket
import msvcrt
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("El nombre del dispositivo es: " + hostname)
print("La dirección IP es: " + ip)
msvcrt.getch()