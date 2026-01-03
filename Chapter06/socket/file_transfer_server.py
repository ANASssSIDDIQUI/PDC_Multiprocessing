import socket

def start_file_server():
    port = 60000
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, port))
    s.listen(5)
    print('File Server listening on port 60000...')

    while True:
        conn, addr = s.accept()
        print(f'Got connection from {addr}')
        
        # Read and send the file content
        try:
            with open('mytext.txt', 'rb') as f:
                data = f.read(1024)
                while data:
                    conn.send(data)
                    data = f.read(1024)
            print("File sent successfully.")
            conn.send(b'\r\n->Thank you for connecting')
        except FileNotFoundError:
            conn.send(b"Error: mytext.txt not found.")
            
        conn.close()

if __name__ == "__main__":
    start_file_server()