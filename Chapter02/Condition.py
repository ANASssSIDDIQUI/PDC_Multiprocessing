import threading,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

cond=threading.Condition()
result=None

def producer():
    global result
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    with cond:
        result=(v,end-start)
        cond.notify()

def consumer():
    global result
    with cond:
        while result is None:
            cond.wait()
        print("LCM",result[0],"Time",result[1])

if __name__=="__main__":
    p=threading.Thread(target=producer)
    c=threading.Thread(target=consumer)
    c.start()
    p.start()
    p.join()
    c.join()
