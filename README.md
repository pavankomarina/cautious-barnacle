# Concurrency in Python
This repository contains working examples of multithreading and multiprocessing libraries in python

Before going through the code, lets first understand what is concurrency and parallelism

## Concurrency vs Parallelism

## C O N C U R R E N C Y

- Ability of program to be broken into parts that can run independently of each other.(deals multiple things at once)
- Multiple threads will be spawned to execute the tasks.(Multi-threading)
- Mainly used for tasks which are IO dependent
- Can be executed in single core machine
- Python module used : `threading`

### GIL(Global Interpreter Lock)

  It is a mechanism that limits Python to only execute one thread at a time.

  Yes, you are reading right. Technically we can't achieve multithreading in Python because of its implementation in CPython. You can use other python
  implementations like Jython, IronPython for it. Since we use multithreading for IO dependent tasks , this will not be major issue and multithreading
  will definitely improve application performance.

## P A R A L L E L I S M 

- Tasks are divided into smaller sub-tasks that are processed seemingly simultaneously or parallel(does multiple things at once)
- Multiple processes will be spawned to execute the tasks.(Multi-processing)
- Mainly used for tasks which are CPU dependent
- Requires multi-core machine
- Python module : `multiprocessing`

## Required Versions
- Python 3.9
- Django 3.2


## Examples
- Threading examples can be found under `threading_examples`
