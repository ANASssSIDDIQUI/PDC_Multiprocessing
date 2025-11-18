import threading,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

sem=threading.Semaphore(2)

def worker(i):
    sem.acquire()
    start=time.time()
    v=lcm(12,18)
    time.sleep(0.1)
    end=time.time()
    print("Worker",i,"LCM",v,"Time",end-start)
    sem.release()

if __name__=="__main__":
    threads=[threading.Thread(target=worker,args=(i,)) for i in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
