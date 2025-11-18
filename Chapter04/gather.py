from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

gcd = lambda a,b: a if b==0 else gcd(b,a%b)
lcm = lambda a,b: a*b//gcd(a,b)

start = time.time()
v = lcm(12,18)
end = time.time()

result = comm.gather((v,end-start), root=0)
if rank == 0:
    print("Gathered results:", result)
