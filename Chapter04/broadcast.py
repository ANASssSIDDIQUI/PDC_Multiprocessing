from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

gcd = lambda a,b: a if b==0 else gcd(b,a%b)
lcm = lambda a,b: a*b//gcd(a,b)

if rank == 0:
    start = time.time()
    value = (lcm(12,18), time.time()-start)
else:
    value = None

value = comm.bcast(value, root=0)
print(f"Rank {rank} received LCM {value[0]}, Time {value[1]}")
