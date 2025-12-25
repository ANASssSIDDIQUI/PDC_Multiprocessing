import asyncio

# --- Functions from your main_code.py integrated into tasks ---
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# --- Chapter 05: Task Manipulation ---

async def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        print(f'Asyncio.Task: Compute factorial({i})')
        # yield from asyncio.sleep(1) is replaced by await
        await asyncio.sleep(1)
        fact *= i
    print(f'Asyncio.Task - factorial({number}) = {fact}')
    return fact

async def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print(f'Asyncio.Task: Compute fibonacci({i})')
        await asyncio.sleep(1)
        a, b = b, a + b
    print(f'Asyncio.Task - fibonacci({number}) = {a}')
    return a

async def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print(f'Asyncio.Task: Compute binomial_coefficient({i})')
        await asyncio.sleep(1)
    
    # Demonstration of using your main_code GCD logic within a task
    check_gcd = gcd(int(result), n)
    print(f'Asyncio.Task - binomial_coefficient({n}, {k}) = {result} (GCD with n: {check_gcd})')
    return result

async def main():
    print("--- Starting Parallel Task Execution ---")
    
    # In modern Python, create_task is the preferred way to wrap coroutines
    # Tasks start running immediately when they are created
    task1 = asyncio.create_task(factorial(10))
    task2 = asyncio.create_task(fibonacci(10))
    task3 = asyncio.create_task(binomial_coefficient(20, 10))

    task_list = [task1, task2, task3]

    # asyncio.wait returns a set of completed and pending tasks
    done, pending = await asyncio.wait(task_list)
    
    for task in done:
        print(f"Task finished with result: {task.result()}")

if __name__ == '__main__':
    # asyncio.run handles the event loop lifecycle automatically
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    print("--- All Tasks Completed ---")