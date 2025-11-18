import multiprocessing, time

def gcd(a,b):
    while b: a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def worker(barrier,i):
    barrier.wait()
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    print("Process",i,"LCM",v,"Time",end-start)

if __name__=="__main__":
    barrier = multiprocessing.Barrier(3)
    processes = [multiprocessing.Process(target=worker, args=(barrier,i)) for i in range(3)]
    for p in processes: p.start()
    for p in processes: p.join()
