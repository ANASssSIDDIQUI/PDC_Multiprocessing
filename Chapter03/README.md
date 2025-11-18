# Chapter 3 – Multiprocessing Concepts with GCD & LCM

## 📘 Overview
This chapter implements **GCD and LCM computations** using Python and demonstrates **multiprocessing and inter-process communication concepts**.  
Each concept is applied to the same LCM + GCD computation to understand **process management, communication, and synchronization** in practice.

---

## 📌 Concepts Implemented

1. **Communication with Pipe**  
   - Demonstrates sending and receiving data between two processes using `multiprocessing.Pipe()`.  
   - One process computes LCM and sends the result; another process receives it.

2. **Communication with Queue**  
   - Producer-consumer pattern using `multiprocessing.Queue()`.  
   - Allows multiple processes to safely put and get LCM results.

3. **Killing Processes**  
   - Demonstrates how to **terminate a process** before it completes.  
   - Useful for stopping runaway or unnecessary processes.

4. **Naming Processes**  
   - Assign custom names to processes for better identification in logs.  
   - Shows `multiprocessing.current_process().name`.

5. **Process in Subclass**  
   - Implements a subclass of `multiprocessing.Process`.  
   - Override `run()` method to compute LCM.  
   - Demonstrates object-oriented approach to multiprocessing.

6. **Process Pool**  
   - Uses `multiprocessing.Pool` to execute multiple LCM computations concurrently.  
   - Efficient for batch processing tasks.

7. **Process Barrier**  
   - Synchronizes multiple processes using `multiprocessing.Barrier()`.  
   - Ensures all processes reach a certain point before proceeding.

8. **Run Background Process (no daemon)**  
   - Starts a process in the background with `daemon=False`.  
   - The main program waits for the process to complete.

9. **Run Background Process (daemon)**  
   - Starts a process in the background with `daemon=True`.  
   - The process runs in the background while the main program continues.

10. **Spawning Process Namespace**  
    - Uses `multiprocessing.Manager().Namespace()` to share variables between processes.  
    - One process computes LCM and stores result in the shared namespace.

11. **Spawning Process (multiple with Manager list)**  
    - Uses `multiprocessing.Manager().list()` to store results from multiple processes.  
    - Demonstrates spawning multiple processes and collecting their outputs safely.

---

## 📂 Files Included
| File | Concept Implemented |
|------|-------------------|
| `pipe_lcm.py` | Communication with Pipe |
| `queue_lcm.py` | Communication with Queue |
| `kill_process_lcm.py` | Killing Processes |
| `name_process_lcm.py` | Naming Processes |
| `subclass_process_lcm.py` | Process in Subclass |
| `pool_lcm.py` | Process Pool |
| `barrier_process_lcm.py` | Process Barrier |
| `background_process_lcm.py` | Run Background Process (no daemon) |
| `daemon_process_lcm.py` | R

---

## 🧮 Execution Time
- Each code snippet measures the execution time for LCM computation using `time.time()`.  
- Demonstrates performance and timing of **multiprocessing operations**.

---

## 🖥 Example Output
- Task 0 LCM 36 Time 0.0000012
- Task 1 LCM 36 Time 0.0000011
- Task 2 LCM 36 Time 0.0000013


---

## 🎯 Learning Objectives
- Understand **process creation, naming, and management**.  
- Implement **inter-process communication** using **Pipe, Queue, and Manager objects**.  
- Apply **process synchronization** using **Barrier**.  
- Run **background processes** (daemon and non-daemon).  
- Handle **process termination** and safety.  
- Measure and analyze **execution time** for multiprocessing operations.  

---

## 🚀 Future Extensions
- Integrate **threading + multiprocessing hybrid programs**.  
- Extend to compute LCM/GCD for **large datasets with multiple processes**.  
- Benchmark **process pool vs individual process spawning**.  
- Build a **distributed computation module** for multi-machine execution.
