import asyncio
import sys
from random import randint

# --- Original main_code.py Functions ---
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# --- Chapter 05: Finite State Machine Implementation ---

async def start_state():
    print('Start State: Initializing FSM...\n')
    input_value = randint(0, 1)
    await asyncio.sleep(1) # Non-blocking sleep

    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)

    print(f'Resume of the Transition:\nStart State calling {result}')

async def state1(transition_value):
    # Demonstrate functionality using GCD
    val = gcd(48, 18)
    output_value = f'State 1 (GCD context: {val}) with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating State 1...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)

    return output_value + f'State 1 calling {result}'

async def state2(transition_value):
    # Demonstrate functionality using LCM
    val = lcm(12, 15)
    output_value = f'State 2 (LCM context: {val}) with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating State 2...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)

    return output_value + f'State 2 calling {result}'

async def state3(transition_value):
    output_value = f'State 3 with transition value = {transition_value}\n'
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating State 3...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)

    return output_value + f'State 3 calling {result}'

async def end_state(transition_value):
    output_value = f'End State reached with transition value = {transition_value}\n'
    print('...stop computation...')
    return output_value

if __name__ == '__main__':
    print('--- Finite State Machine simulation with Asyncio ---')
    try:
        # Use asyncio.run for Python 3.14 compatibility
        asyncio.run(start_state())
    except KeyboardInterrupt:
        pass
    print('--- Simulation Finished ---')