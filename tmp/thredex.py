
import threading
import time

def thread1_function():
    print("Thread 1 is running...")
    time.sleep(5)
    print("Thread 1 is about to quit...")
    # Thread 1 will naturally exit here since the function ends

def thread2_function():
    print("Thread 2 is running...")
    while True:
        print("Thread 2 is still running...")
        time.sleep(2)

# Creating the two threads
thread1 = threading.Thread(target=thread1_function)
thread2 = threading.Thread(target=thread2_function)

# Starting the threads
thread1.start()
thread2.start()

# Joining thread1 to ensure the main thread waits for it to finish
thread1.join()

# The main thread will continue, and thread2 will keep running in the background
print("Thread 1 has quit, but Thread 2 is still running.")
