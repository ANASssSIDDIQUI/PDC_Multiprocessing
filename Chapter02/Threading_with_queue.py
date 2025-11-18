import threading,queue,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

q=queue.Queue()

def worker():
    while True:
        try:
            a,b=q.get(timeout=0.2)
        except:
            break
        start=time.time()
        v=lcm(a,b)
        end=time.time()
        print("LCM",v,"Time",end-start)
        q.task_done()

if __name__=="__main__":
    for _ in range(6):
        q.put((12,18))
    threads=[threading.Thread(target=worker) for _ in range(3)]
    for t in threads: t.start()
    q.join()
    for t in threads: t.join()
