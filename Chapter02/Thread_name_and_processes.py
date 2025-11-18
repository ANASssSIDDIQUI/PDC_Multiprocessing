import threading,multiprocessing,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def thr_job():
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    print("thread",threading.current_thread().name,v,end-start)

def proc_job():
    start=time.time()
    v=lcm(12,18)
    end=time.time()
    print("process",multiprocessing.current_process().name,v,end-start)

if __name__=="__main__":
    t=threading.Thread(target=thr_job,name="MyThread")
    p=multiprocessing.Process(target=proc_job,name="MyProcess")
    t.start()
    p.start()
    t.join()
    p.join()
