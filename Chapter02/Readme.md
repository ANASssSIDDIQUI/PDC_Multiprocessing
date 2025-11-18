# Chapter 2 — Thread-Based Parallelism (Practical Implementation)

## 📘 Overview
This chapter implements **GCD and LCM computations** using Python and demonstrates **parallel and concurrent programming concepts**. Each concept is applied to the same LCM + GCD computation to help understand **threading, synchronization, and multiprocessing** in practice.

---

## 📌 Concepts Implemented

1. **Threading**  
   - Basic threads to compute LCM concurrently.  
   - Multiple threads perform the same LCM computation simultaneously.  

2. **Barrier**  
   - Threads wait at a barrier before computing LCM.  
   - Ensures synchronized start for multiple threads.  

3. **Condition**  
   - Threads communicate using `threading.Condition()`.  
   - One thread signals when LCM is ready; another waits to consume the result.  

4. **Event**  
   - Threads synchronize via `threading.Event()`.  
   - LCM computation waits until the event is triggered.  

5. **RLock (Reentrant Lock)**  
   - Allows nested locks in the same thread.  
   - Demonstrates thread-safe recursive computations of LCM/GCD.  

6. **Semaphore**  
   - Limits number of threads running LCM computations concurrently.  
   - Helps control access to limited resources.  

7. **Thread Lock**  
   - Uses `threading.Lock()` to safely update shared results while computing LCM.  

8. **Thread Lock with Definition**  
   - Custom lock function returns a lock object.  
   - Ensures thread-safe LCM computation when multiple threads update a shared variable.  

9. **Thread Class (Definition)**  
   - Subclass of `threading.Thread` that overrides `run()` to compute LCM.  
   - Demonstrates object-oriented thread implementation.  

10. **Thread Determine (alive, ident)**  
    - Checks thread state (`is_alive()` and `ident`) during LCM computation.  

11. **Thread Name & Processes**  
    - Shows thread names and process names executing LCM.  
    - Demonstrates combination of threading + multiprocessing.  

12. **Threading with Queue**  
    - Producer-consumer model using `queue.Queue()`.  
    - Threads consume pairs of numbers and compute LCM concurrently.  

---

## 📂 Files Included
| File | Concept Implemented |
|------|-------------------|
| `barrier_lcm.py` | Barrier |
| `condition_lcm.py` | Condition |
| `event_lcm.py` | Event |
| `rlock_lcm.py` | Reentrant Lock |
| `semaphore_lcm.py` | Semaphore |
| `threading_lcm.py` | Basic Threading |
| `threadlock_lcm.py` | Thread Lock |
| `threadlock_def_lcm.py` | Thread Lock with Definition |
| `thread_class_lcm.py` | Thread Class (Definition) |
| `thread_determine_lcm.py` | Thread Determine |
| `thread_process_lcm.py` | Thread Name & Process Name |
| `thread_queue_lcm.py` | Threading with Queue |

---

## 🧮 Execution Time
- Each snippet measures execution time for the LCM computation using `time.time()`.  
- Demonstrates performance measurement of **parallel/concurrent execution**.  

---

## 🖥 Example Output
- Thread 0 LCM 36 Time 0.00000123
- Thread 1 LCM 36 Time 0.00000120
- Thread 2 LCM 36 Time 0.00000122


---

## 🎯 Learning Objectives
- Understand **threading, synchronization, locks, semaphores, events, and barriers**.  
- Apply **parallel programming concepts** to a real computation (LCM + GCD).  
- Measure **execution times** for parallel operations.  
- Demonstrate **thread-safe and process-safe code**.  
- Build modular and maintainable Python code for concurrent tasks.  

---

## 🚀 Future Extensions
- Add **multiprocessing with shared memory** for LCM of large lists.  
- Combine multiple concepts in one program (e.g., Barrier + Semaphore + Queue).  
- Benchmark performance with increasing thread/process counts.  
- Expand to **distributed systems** using sockets or RPC.  
