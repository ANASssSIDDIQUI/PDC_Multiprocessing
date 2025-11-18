import multiprocessing, time

def gcd(a,b):
    while b: a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def worker(ns):
    start=time.time()
    ns.lcm = lcm(12,18)
    ns.time = time.time() - start

if __name__=="__main__":
    manager = multiprocessing.Manager()
    ns = manager.Namespace()
    p = multiprocessing.Process(target=worker, args=(ns,))
    p.start()
    p.join()
    print("LCM",ns.lcm,"Time",ns.time)
