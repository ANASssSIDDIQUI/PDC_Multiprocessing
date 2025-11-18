# Python Multiprocessing & Multithreading Example

This project demonstrates how to implement **multiprocessing** and **multithreading** in Python to speed up CPU-bound and I/O-bound tasks.  
It also compares execution times to show how parallelism can improve performance.

---

## Project Structure

├── sandwich.py # Contains the main function 'make_sandwich' (your task)
├── multiprocessing_demo.py # Runs the function using multiprocessing
├── multithreading_demo.py # Runs the function using multithreading
└── README.md # You're reading this file

---

## How It Works

- **`sandwich.py`** defines a function that simulates a CPU-heavy or time-consuming task (like mathematical computation or array processing).  
- **`main_multiprocess.py`** creates multiple processes to execute the function in parallel — ideal for **CPU-bound tasks**.  
- **`main_multithread.py`** creates multiple threads to execute the same function concurrently — suitable for **I/O-bound tasks**.  

Each file measures and prints execution time to show the performance difference.

---

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/parallel-processing-demo.git
   cd parallel-processing-demo


## Requirements

Python 3.8+

No external libraries required

## Key Concepts Demonstrated

multiprocessing.Process and join()
threading.Thread and join()
Measuring execution time using time module
CPU-bound vs I/O-bound performance
Avoiding import shadowing with standard libraries
Safe multiprocessing with if __name__ == "__main__":


## Author

Anas Ahmed Siddiqui
Computer Science Student @ Usman Institute of Engineering & Technology
Demonstrating practical parallel programming concepts in Python using both multiprocessing and multithreading.

## License

This project is open source and available under the MIT License.

