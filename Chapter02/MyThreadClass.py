import threading,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def task(name):
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    print(name,"LCM",v,"Time",end-start)

if __name__=="__main__":
    t1=threading.Thread(target=task,args=("T1",))
    t2=threading.Thread(target=task,args=("T2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
