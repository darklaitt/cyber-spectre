import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("localhost", 9001))
print("UDP-сервер ожидает данные...")

while True:
    data, addr = udp_socket.recvfrom(1024)
    print(f"Получено от {addr}: {data.decode()}")
