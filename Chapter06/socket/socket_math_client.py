import socket

def start_client():
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999

    try:
        s.connect((host, port))
        
        # Numbers to calculate
        num1, num2 = 48, 18
        message = f"{num1},{num2}"
        
        print(f"Sending {num1} and {num2} to server...")
        s.send(message.encode())
        
        # Receive results
        result = s.recv(1024).decode()
        print(f"Server response: {result}")
        
    finally:
        s.close()

if __name__ == "__main__":
    start_client()