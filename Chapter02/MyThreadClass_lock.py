import threading,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

lock=threading.Lock()
results=[]

def incr(i):
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    lock.acquire()
    results.append((i,v,end-start))
    lock.release()

if __name__=="__main__":
    threads=[threading.Thread(target=incr,args=(i,)) for i in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(results)
    