from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

gcd = lambda a,b: a if b==0 else gcd(b,a%b)
lcm = lambda a,b: a*b//gcd(a,b)

dims = [size]
cart = comm.Create_cart(dims)
coords = cart.Get_coords(rank)

start = time.time()
v = lcm(12,18)
end = time.time()
print(f"Rank {rank}, coords {coords}, LCM {v}, Time {end-start}")
