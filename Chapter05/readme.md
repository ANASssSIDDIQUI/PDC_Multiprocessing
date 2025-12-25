# Chapter 05: Asynchronous and Concurrent Computing

This chapter explores the orchestration of tasks using `asyncio` for non-blocking I/O and `concurrent.futures` for parallel CPU-bound execution. The implementations utilize the GCD and LCM logic from the core project.

## Implementation Overview

### 1. [asyncio_and_futures038.py](./asyncio_and_futures038.py)
Demonstrates the use of `asyncio.Future` and callbacks. It schedules math operations and triggers a notification immediately upon completion without blocking the main thread.

### 2. [asyncio_coroutine038.py](./asyncio_coroutine038.py)
Simulates a **Finite State Machine (FSM)**. It uses asynchronous coroutines to transition between states, where each state performs a specific mathematical evaluation.

### 3. [asyncio_event_loop038.py](./asyncio_event_loop038.py)
Focuses on low-level event loop management. It uses `call_soon` and `call_later` to schedule recursive tasks (Task A -> B -> C) until a specified timeout.

### 4. [asyncio_task_manipulation038.py](./asyncio_task_manipulation038.py)
Wraps coroutines into `Task` objects to execute Factorial, Fibonacci, and Binomial Coefficient calculations in parallel.

### 5. [concurrent_futures_pooling038.py](./concurrent_futures_pooling038.py)
A performance comparison of execution models for CPU-intensive tasks.

## Performance Comparison

| Method | Execution Model | Best Use Case | Logic Speed |
| :--- | :--- | :--- | :--- |
| **Sequential** | Single-threaded, blocking | Simple, linear scripts | Slowest |
| **Thread Pool** | Shared memory, context switching | I/O-bound tasks (Network/Disk) | Moderate |
| **Process Pool** | Multiple CPU cores, parallel | CPU-bound tasks (GCD/LCM/Math) | Fastest |

## Environment Requirements
* Python 3.10+ (Tested on 3.14)
* Standard Library: `asyncio`, `concurrent.futures`, `time`, `random`

## Usage
To run the pooling comparison:
```bash
python concurrent_futures_pooling038.py