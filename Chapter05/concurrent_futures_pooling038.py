import concurrent.futures
import time
import sys

# --- Functions from your main_code.py ---
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Using your existing logic as the "heavy" task
    return (a * b) // gcd(a, b)

# --- Chapter 05: Pooling Implementation ---

number_list = list(range(1, 11))

def evaluate_lcm(item):
    """A CPU-bound task that calculates LCM and simulates a workload."""
    # Simulating a heavy calculation loop
    count = 0
    for i in range(0, 1000000):
        count += 1
    
    # Calculate LCM using your project logic
    result = lcm(item, 100)
    print(f'Item {item}, LCM with 100 is {result}')
    return result

if __name__ == '__main__':
    # 1. Sequential Execution
    # Note: time.clock() is replaced by time.perf_counter() for Python 3.14
    start_time = time.perf_counter()
    print("Starting Sequential Execution...")
    for item in number_list:
        evaluate_lcm(item)
    print(f'Sequential Execution finished in {time.perf_counter() - start_time:.4f} seconds\n')

    # 2. Thread Pool Execution
    # Useful for I/O bound tasks
    start_time = time.perf_counter()
    print("Starting Thread Pool Execution...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # submit() schedules the callable to be executed
        for item in number_list:
            executor.submit(evaluate_lcm, item)
    print(f'Thread Pool Execution finished in {time.perf_counter() - start_time:.4f} seconds\n')

    # 3. Process Pool Execution
    # Useful for CPU-bound tasks (Parallelism)
    start_time = time.perf_counter()
    print("Starting Process Pool Execution...")
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_lcm, item)
    print(f'Process Pool Execution finished in {time.perf_counter() - start_time:.4f} seconds\n')