from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

gcd = lambda a,b: a if b==0 else gcd(b,a%b)
lcm = lambda a,b: a*b//gcd(a,b)

send_data = [(12+rank,18+rank+i) for i in range(size)]
recv_data = comm.alltoall(send_data)
start = time.time()
v = [lcm(a,b) for a,b in recv_data]
end = time.time()
print(f"Rank {rank} computed LCMs {v}, Time {end-start}")
