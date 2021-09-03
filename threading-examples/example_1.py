# description:  
# This program demonstrates the use of threading concepts in python. 
# author : Pavan Kalyan Komarina

import time
import threading

# a simple method that sends message to the sender
def send_message(message: str) -> None:
    print(f"Sending message : {message}")
    time.sleep(1)
    print(f"Message : {message} sent succesfully")


message_list = ["message_1", "message_2", "message_3"]

start = time.perf_counter()
for message in message_list:
    send_message(message)
print(f"\nTotal Time taken for synchronous execution: {time.perf_counter() - start} seconds!")
print("\n")

# using threads to perform the tasks!
start = time.perf_counter()

threads = []  # store all the created threads
for message in message_list:
    t = threading.Thread(target=send_message, args=(message,))
    threads.append(t)
    t.start()

# join the threads to main thread so program execution will wait
# until the threads will finish their tasks!

main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    t.join()
print(f"\nTotal Time taken using threads : {time.perf_counter() - start} seconds!\n")


# Output: 
'''
Sending message : message_1
Message : message_1 sent succesfully
Sending message : message_2
Message : message_2 sent succesfully
Sending message : message_3
Message : message_3 sent succesfully

Total Time taken for synchronous execution: 3.004097300000012 seconds!


Sending message : message_1
Sending message : message_2
Sending message : message_3
Message : message_1 sent succesfully
Message : message_2 sent succesfully
Message : message_3 sent succesfully

Total Time taken using threads : 1.0074803000002248 seconds!
'''