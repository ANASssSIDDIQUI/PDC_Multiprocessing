from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

gcd = lambda a,b: a if b==0 else gcd(b,a%b)
lcm = lambda a,b: a*b//gcd(a,b)

# Deadlock if both try to recv first
if rank == 0:
    start=time.time()
    comm.send(lcm(12,18), dest=1)
    v = comm.recv(source=1)
    end=time.time()
    print(f"Rank 0 received {v}, Time {end-start}")
elif rank == 1:
    start=time.time()
    v = comm.recv(source=0)
    comm.send(lcm(12,18), dest=0)
    end=time.time()
    print(f"Rank 1 received {v}, Time {end-start}")
