from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

gcd = lambda a,b: a if b==0 else gcd(b,a%b)
lcm = lambda a,b: a*b//gcd(a,b)

if rank == 0:
    start = time.time()
    v = lcm(12,18)
    end = time.time()
    comm.send((v,end-start), dest=1)
elif rank == 1:
    v,t = comm.recv(source=0)
    print(f"Rank {rank} received LCM {v}, Time {t}")
