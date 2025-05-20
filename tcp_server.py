import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9000))
server_socket.listen(5)

print("TCP-сервер запущен на порту 9000")

with open("log.txt", "a") as log_file:
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Клиент подключен: {addr}")
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            print("Получено:", data)
            log_file.write(data + "\n")
            client_socket.sendall("Запись принята.\n".encode('utf-8'))
        client_socket.close()
