import socket

message = input("Введите сообщение для журнала: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9000))
client_socket.sendall(message.encode('utf-8'))
response = client_socket.recv(1024).decode('utf-8')
print("Ответ сервера:", response)
client_socket.close()
