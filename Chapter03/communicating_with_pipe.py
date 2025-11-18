import multiprocessing, time

def gcd(a,b):
    while b: a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def sender(pipe):
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    pipe.send((v,end-start))
    pipe.close()

def receiver(pipe):
    v,t=pipe.recv()
    print("LCM",v,"Time",t)

if __name__=="__main__":
    parent, child = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=sender, args=(child,))
    p2 = multiprocessing.Process(target=receiver, args=(parent,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
