from mpi4py import MPI
import time
import functools

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

gcd = lambda a,b: a if b==0 else gcd(b,a%b)
lcm = lambda a,b: a*b//gcd(a,b)

start = time.time()
v = lcm(12,18)
end = time.time()

total = comm.reduce(v, op=MPI.SUM, root=0)
if rank == 0:
    print("Reduced sum of LCMs:", total, "Time", end-start)
