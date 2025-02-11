# FastSnake

[![Python Package](https://github.com/JeanExtreme002/FastSnake/workflows/Python%20Package/badge.svg)](https://github.com/JeanExtreme002/FastSnake/actions)
[![Pypi](https://img.shields.io/pypi/v/FastSnake?logo=pypi)](https://pypi.org/project/FastSnake/)
[![License](https://img.shields.io/pypi/l/FastSnake)](https://github.com/JeanExtreme002/FastSnake)
[![Platforms](https://img.shields.io/badge/platforms-Windows%20%7C%20Linux-8A2BE2)](https://pypi.org/project/FastSnake/)
[![Python Version](https://img.shields.io/badge/python-3.7+-yellow)](https://pypi.org/project/FastSnake/)

Tired of having to copy-paste your library code into every solution you write? FastSnake is a command-line tool that allows you to easily create, expand, run and test Python solutions for competitive programming problems.

This project provides useful CLI tools for competitive programming, such as algorithms and data structures, and tools for Codeforces. But you will have to write your own code and library for the problems you want to solve.

## Installing FastSnake:
```
$ pip install FastSnake
```

## Basic Usage:
Starting a contest from Codeforces...
```
$ fastsnake codeforces -sc <contest_id>
```
**Note:** The contest ID can be found at contest URL `https://codeforces.com/contest/<id>`
<br>

Once you have written your solution, test it.
```
$ fastsnake test <problem>
```

You can also create your own generator, at `test_generators` folder, to bruteforce your solution.
```
$ fastsnake test <problem> -g <n_tests>
```

### Starting a Custom Contest
Use the command below to start your own contest.
```
$ fastsnake start-custom-contest <n_problems>
```

### Algorithms and Structures

FastSnake provides some algorithms and structures that can be injected to your final solution. See the sample below:

**Python Solution:**
```py
from fastsnake.algorithms.min_coins import *

coins = []

for x in input().split():
    coins.append(int(x))

value = int(input())

result = min_coins(coins, value)
print(result)
```
Use the argument `--list <algorithms | structures | external>` to see all algorithms and structures provided by FastSnake.

**Injecting the algorithm to the final solution...**
```
$ fastsnake compile main.py
```
Check out the code of the generated Python module.
<br>

### Testing and Compiling:
You may test and compile your solution using the command below:
```
$ fastsnake test <problem> -c
```
If the solution was accepted at all test cases, it will be compiled.


### Adding External Modules:
You may also add your own modules to the external package of fastsnake.
```
$ fastsnake add-external <path | url> --name <module_name> [--url]
```
For downloading the module from web, use the flag `--url`.
