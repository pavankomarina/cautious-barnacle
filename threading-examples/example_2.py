# Problem Statement.
# lets say, there are two tasks which are IO/network bound and are dependent on each other.
# message should process first and should be sent only after processed.
# author : Pavan Kalyan Komarina

import time
import threading

# a simple method that formats message according to a defined format.
def process_message(message: str) -> None:
    print(f"Processing message : {message}")
    # can be I/O or network bound. delaying by 1 second.
    time.sleep(1)
    print(f"Message : {message} processed succesfully!")

# a simple method that sends message to the sender
def send_message(message: str) -> None:
    print(f"Sending message : {message}")
    # can be I/O or network bound. delaying by 3 seconds.
    time.sleep(3)
    print(f"Message : {message} sent succesfully")

message_list = ["message_1", "message_2", "message_3"]

start = time.perf_counter()
for message in message_list:
    process_message(message)
    send_message(message)
print(f"\nTotal Time taken for synchronous execution: {time.perf_counter() - start} seconds!\n")

# # using threads to perform the tasks!
start = time.perf_counter()

for message in message_list:
    t1 = threading.Thread(target=process_message, args=(message,))
    t1.start()

# calling functions separately as those are dependent on each other.
# message function should be called only after processing.
main_thread = threading.current_thread()
for _thread in threading.enumerate():
    if _thread is main_thread:
        continue
    _thread.join()

for message in message_list:
    t2 = threading.Thread(target=send_message, args=(message,))
    t2.start()
    

# # join the threads to main thread so program execution will wait
# # until the threads will finish their tasks!

# # print the total active threads
# # MainThread + total spawned threads
# print(f"\nCurrent thread count: {threading.active_count()}\n")

main_thread = threading.current_thread()
for _thread in threading.enumerate():
    if _thread is main_thread:
        continue
    _thread.join()
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

Current thread count: 4

Message : message_1 sent succesfully
Message : message_2 sent succesfully
Message : message_3 sent succesfully

Total Time taken using threads : 1.0074803000002248 seconds!
'''