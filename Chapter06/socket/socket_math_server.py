import socket

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def start_server():
    port = 9999
    # Create a TCP/IP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.bind((host, port))
    
    s.listen(5)
    print(f'Math Server listening on {host}:{port}...')

    while True:
        conn, addr = s.accept()
        print(f'Connected by {addr}')
        
        # Receive data from client (format: "num1,num2")
        data = conn.recv(1024).decode()
        if not data:
            break
            
        try:
            n1, n2 = map(int, data.split(','))
            res_gcd = gcd(n1, n2)
            res_lcm = lcm(n1, n2)
            
            response = f"GCD: {res_gcd}, LCM: {res_lcm}"
            conn.send(response.encode())
        except ValueError:
            conn.send("Error: Please send numbers in 'num1,num2' format".encode())
            
        conn.close()

if __name__ == "__main__":
    start_server()