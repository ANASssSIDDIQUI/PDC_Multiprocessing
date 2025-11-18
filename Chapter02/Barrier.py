import threading, time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def worker(barr,i):
    barr.wait()
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    print("Thread",i,"LCM",v,"Time",end-start)

if __name__=="__main__":
    barr=threading.Barrier(3)
    threads=[threading.Thread(target=worker,args=(barr,i)) for i in range(3)]
    for t in threads: t.start()
    for t in threads: t.join()
