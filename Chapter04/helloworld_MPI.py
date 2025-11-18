from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

start = time.time()
gcd = lambda a,b: a if b==0 else gcd(b,a%b)
lcm = lambda a,b: a*b//gcd(a,b)
v = lcm(12,18)
end = time.time()

print(f"Hello from rank {rank} of {size}, LCM {v}, Time {end-start}")
