import threading,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def make_lock():
    return threading.Lock()

lock=make_lock()
value=0

def add():
    global value
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    with lock:
        value+=v
    print("Time",end-start)

if __name__=="__main__":
    threads=[threading.Thread(target=add) for _ in range(4)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("value",value)
