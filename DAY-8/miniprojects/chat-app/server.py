import socket
import threading

def handle_client(client_socket, client_address):
    def receive_messages():
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"\n{client_address}:", data.decode('utf-8'))
            except:
                break

    threading.Thread(target=receive_messages, daemon=True).start()

    # Server can also send messages back interactively
    while True:
        message = input("Server: ")
        client_socket.sendall(message.encode('utf-8'))

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server listening...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True).start()

if __name__ == "__main__":
    main()