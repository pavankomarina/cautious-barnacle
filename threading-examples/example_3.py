# Problem statement:
# When two or more threads accessing the same resources , data race might happen
# Locking is used to resolve these type of issues
# Following example demonstrates the locking mechanism in Python.

import threading

total_count = 0
book_count = 0
pencil_count = 0

