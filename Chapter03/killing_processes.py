import multiprocessing, time

def gcd(a,b):
    while b: a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def worker():
    try:
        start=time.time()
        v=lcm(12,18)
        end=time.time()
        print("LCM",v,"Time",end-start)
    except:
        print("Process terminated")

if __name__=="__main__":
    p = multiprocessing.Process(target=worker)
    p.start()
    p.terminate()
    p.join()
    print("Process killed")
