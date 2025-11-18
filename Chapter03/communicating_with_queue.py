import multiprocessing, queue, time

def gcd(a,b):
    while b: a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def producer(q):
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    q.put((v,end-start))

def consumer(q):
    v,t=q.get()
    print("LCM",v,"Time",t)

if __name__=="__main__":
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
