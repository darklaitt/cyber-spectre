import socket
import time
import random

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    emf_value = random.uniform(0, 5)
    message = f"EMF: {emf_value:.2f}"
    udp_socket.sendto(message.encode(), ("localhost", 9001))
    print("Отправлено:", message)
    time.sleep(1)
