from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

gcd = lambda a,b: a if b==0 else gcd(b,a%b)
lcm = lambda a,b: a*b//gcd(a,b)

data = None
if rank == 0:
    data = [(i+12,i+18) for i in range(size)]
item = comm.scatter(data, root=0)
start = time.time()
v = lcm(*item)
end = time.time()
print(f"Rank {rank} computed LCM {v}, Time {end-start}")
