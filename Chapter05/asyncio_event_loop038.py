import asyncio
import random
import sys

# --- Original main_code.py Functions ---
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# --- Chapter 05: Event Loop Task Scheduling ---

def task_A(end_time, loop):
    """Calculates GCD and schedules Task B."""
    print(f"[Task A] Calculating GCD: {gcd(48, 18)}")
    
    # Check if we still have time left in the loop
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_B, end_time, loop)
    else:
        print("Time limit reached. Stopping Loop.")
        loop.stop()

def task_B(end_time, loop):
    """Calculates LCM and schedules Task C."""
    print(f"[Task B] Calculating LCM: {lcm(12, 15)}")
    
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_C, end_time, loop)
    else:
        print("Time limit reached. Stopping Loop.")
        loop.stop()

def task_C(end_time, loop):
    """Prints status and schedules Task A."""
    print(f"[Task C] System status: Operational. Time: {loop.time():.2f}")
    
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, task_A, end_time, loop)
    else:
        print("Time limit reached. Stopping Loop.")
        loop.stop()

if __name__ == '__main__':
    print("--- Asyncio Event Loop Scheduling (Chapter 05) ---")
    
    # Modern way to handle the loop in Python 3.14 to avoid RuntimeError
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        # Set loop to run for 10 seconds (reduced from 60 for testing)
        end_loop = loop.time() + 10
        
        # Schedule the first task to run as soon as the loop starts
        loop.call_soon(task_A, end_loop, loop)
        
        # Keep the loop running until loop.stop() is called
        loop.run_forever()
    finally:
        loop.close()
        print("--- Event Loop Closed ---")