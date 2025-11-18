import threading,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def job():
    time.sleep(0.1)
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    print("LCM",v,"Time",end-start)

if __name__=="__main__":
    t=threading.Thread(target=job)
    print("alive1",t.is_alive())
    t.start()
    print("alive2",t.is_alive())
    print("ident",t.ident)
    t.join()
    print("alive3",t.is_alive())
