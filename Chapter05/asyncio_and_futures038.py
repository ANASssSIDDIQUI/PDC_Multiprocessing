import asyncio
import sys

# --- Original main_code.py Functions ---
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# --- Chapter 05 Coroutines (Updated Syntax) ---
async def first_coroutine(future, num1, num2):
    print(f"Coroutine 1: Calculating GCD for {num1}, {num2}...")
    await asyncio.sleep(2) 
    result = gcd(num1, num2)
    future.set_result(f"First coroutine (GCD) result = {result}")

async def second_coroutine(future, num1, num2):
    print(f"Coroutine 2: Calculating LCM for {num1}, {num2}...")
    await asyncio.sleep(4) 
    result = lcm(num1, num2)
    future.set_result(f"Second coroutine (LCM) result = {result}")

def got_result(future):
    print(f"Callback Notification: {future.result()}")

async def main():
    # Handle command line arguments
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except (IndexError, ValueError):
        num1, num2 = 12, 18
        print(f"Usage: python file.py <int> <int>. Using defaults: {num1}, {num2}")

    # In modern Python, we create futures within the running loop
    loop = asyncio.get_running_loop()
    future1 = loop.create_future()
    future2 = loop.create_future()

    # Add callbacks
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    print("--- Starting Concurrent Tasks ---")
    # Schedule both tasks to run concurrently
    await asyncio.gather(
        first_coroutine(future1, num1, num2),
        second_coroutine(future2, num1, num2)
    )

if __name__ == '__main__':
    # asyncio.run handles the loop lifecycle automatically
    asyncio.run(main())
    print("--- Tasks Finished ---")