import multiprocessing, time

def gcd(a,b):
    while b: a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def worker():
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    print("LCM",v,"Time",end-start)

if __name__=="__main__":
    p = multiprocessing.Process(target=worker)
    p.daemon = False
    p.start()
    print("Main process continues")
    p.join()
