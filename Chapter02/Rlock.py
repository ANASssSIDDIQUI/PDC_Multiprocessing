import threading,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

r=threading.RLock()
count=0

def nested(n):
    global count
    with r:
        count+=1
        if n>0:
            nested(n-1)

if __name__=="__main__":
    start=time.time()
    t=threading.Thread(target=nested,args=(3,))
    t.start()
    t.join()
    v=lcm(12,18)
    end=time.time()
    print("count",count,"LCM",v,"Time",end-start)
