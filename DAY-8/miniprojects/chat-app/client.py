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

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print("\nServer:", data.decode('utf-8'))
        except:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))   # ✅ connect, not bind

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input("You: ")
        client_socket.sendall(message.encode('utf-8'))

if __name__ == "__main__":
    main()