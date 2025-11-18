# Chapter 4 – MPI Concepts with GCD & LCM

## 📘 Overview
This chapter implements **GCD and LCM computations** using Python and **MPI (mpi4py)** to demonstrate various **parallel and distributed computing concepts**.  
Each MPI concept is applied to the same LCM + GCD computation to understand **process communication, synchronization, reduction, and topology** in practice.

---

## 📌 Concepts Implemented

1. **Hello World MPI**  
   - Basic MPI program to print from each rank.  
   - Demonstrates initialization and basic communication.

2. **Point-to-Point Communication**  
   - Uses `comm.send()` and `comm.recv()` for **direct communication** between two ranks.  
   - One process computes LCM and sends the result to another.

3. **Broadcast**  
   - Root process sends LCM to all other ranks using `comm.bcast()`.  
   - Ensures all processes have the same data.

4. **Scatter**  
   - Root process distributes pairs of numbers to all ranks using `comm.scatter()`.  
   - Each process computes LCM for its portion.

5. **Gather**  
   - Processes send their computed LCMs to the root using `comm.gather()`.  
   - Root collects all results for aggregation.

6. **All-to-All Communication**  
   - Each process sends data to every other process using `comm.alltoall()`.  
   - Each rank computes LCMs for the received data.

7. **Reduction**  
   - Aggregates results across processes using `comm.reduce()`.  
   - Example: summing all LCM values at root rank.

8. **Deadlock Example**  
   - Demonstrates potential deadlock with improper send/recv order.  
   - Teaches safe communication patterns.

9. **Virtual Topology (Cartesian)**  
   - Uses `comm.Create_cart()` to create a **virtual Cartesian topology**.  
   - Processes have coordinates for structured communication.

---

## 📂 Files Included
| File | Concept Implemented |
|------|-------------------|
| `helloworld_mpi.py` | Hello World MPI |
| `pointtopoint_mpi.py` | Point-to-Point Communication |
| `broadcast_mpi.py` | Broadcast |
| `scatter_mpi.py` | Scatter |
| `gather_mpi.py` | Gather |
| `alltoall_mpi.py` | All-to-All Communication |
| `reduction_mpi.py` | Reduction |
| `deadlock_mpi.py` | Deadlock Example |
| `virtual_topology_mpi.py` | Virtual Topology (Cartesian) |

---

## 🧮 Execution Time
- Each snippet measures **execution time** of LCM computation per rank using `time.time()`.  
- Helps analyze **performance in distributed processes**.

---

## 🖥 Example Output
- Rank 0 computed LCM 36, Time 0.0000012
- Rank 1 computed LCM 36, Time 0.0000011
- Rank 2 computed LCM 36, Time 0.0000013


---

## 🎯 Learning Objectives
- Understand **MPI initialization and rank/size concepts**.  
- Implement **point-to-point and collective communication** (send/recv, broadcast, scatter, gather, alltoall).  
- Handle **process synchronization and deadlocks**.  
- Learn **reduction operations** for aggregating results.  
- Use **virtual topologies** to structure process communication.  
- Measure and analyze **execution time per rank** for distributed computations.  

---

## 🚀 Future Extensions
- Compute **LCM/GCD for large datasets** using MPI across multiple nodes.  
- Combine **MPI + threading** for hybrid parallel programming.  
- Benchmark **collective communication vs point-to-point communication**.  
- Implement **fault-tolerant MPI programs** for real-world distributed computing.
