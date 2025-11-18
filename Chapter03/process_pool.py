import multiprocessing, time

def gcd(a,b):
    while b: a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def task(x):
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    return (x,v,end-start)

if __name__=="__main__":
    with multiprocessing.Pool(3) as pool:
        results = pool.map(task, range(5))
    for r in results:
        print("Task",r[0],"LCM",r[1],"Time",r[2])
