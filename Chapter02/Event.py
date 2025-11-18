import threading,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

ev=threading.Event()

def waiter():
    ev.wait()
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    print("LCM",v,"Time",end-start)

def setter():
    time.sleep(0.2)
    ev.set()

if __name__=="__main__":
    t1=threading.Thread(target=waiter)
    t2=threading.Thread(target=setter)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
