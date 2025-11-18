from sandwich import *
import time
import multiprocessing
import threading

if __name__ == "__main__":
    size = 10000000
    procs = 10
    jobs = []

    #Multiprocessing
    start_time = time.time()
    for i in range (procs):
        out_list = list()
        process = multiprocessing.Process(target=sandwich, args=(size, out_list))
        jobs.append(process)

    for j in jobs:
        j.start()
    
    for j in jobs:
        j.join()

    print("Array processing complete.")
    end_time = time.time()

    print("Multiprocessing time = ", end_time-start_time)

    #Multithreading

    jobs = []
    threads = 10

    start_time = time.time()
    for k in range(threads):
        out_list  = list()
        thread = threading.Thread(target=sandwich, args=(size, out_list))
        jobs.append(thread)

    for l in jobs:
        l.start()

    for l in jobs:
        l.join()

    print("Array processing complete.")
    end_time = time.time()

    print("Threading time = ", end_time-start_time)
    