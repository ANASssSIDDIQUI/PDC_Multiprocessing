import multiprocessing, time

def gcd(a,b):
    while b: a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def worker(i,results):
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    results.append((i,v,end-start))

if __name__=="__main__":
    manager = multiprocessing.Manager()
    results = manager.list()
    processes = [multiprocessing.Process(target=worker, args=(i,results)) for i in range(3)]
    for p in processes: p.start()
    for p in processes: p.join()
    print(list(results))
