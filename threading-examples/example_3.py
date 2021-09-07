# Problem statement:
# When two or more threads accessing the same resources , data race might happen
# Locking is used to resolve these type of issues
# Following example demonstrates the locking mechanism in Python.

import threading

total_count = 0
book_count = 0
pencil_count = 0

class ThreadLockDemo:
    lock = threading.RLock()

    def count_books(self):
        global total_count
        global book_count
        for _ in range(10_000_000):
            self.lock.acquire() # lock the common object
            total_count += 2
            self.lock.release()
            book_count += 1 # only this method uses book_count so no lock required.

    def count_pencils(self):
        global total_count
        global pencil_count
        for _ in range(20_000_000):
            self.lock.acquire() # lock the common object
            total_count += 5
            self.lock.release()
            pencil_count +=1  # only this method uses pencil_count so no lock required.

