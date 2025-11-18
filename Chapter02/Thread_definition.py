import threading,time

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

class MyThread(threading.Thread):
    def run(self):
        start=time.time()
        v=lcm(12,18)
        end=time.time()
        print(self.name,"LCM",v,"Time",end-start)

if __name__=="__main__":
    t=MyThread(name="WorkerThread")
    t.start()
    t.join()
