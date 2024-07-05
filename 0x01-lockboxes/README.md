# Lockboxes Project

## Description

This project involves determining whether all boxes can be unlocked given a list of boxes, each containing keys to other boxes.

## Concepts Needed:

### Lists and List Manipulation:
Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
- [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

### Graph Theory Basics:
Knowledge of graph theory, especially concepts related to traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS), can be helpful as the boxes and keys can be thought of as nodes and edges in a graph.
- [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms)

### Algorithmic Complexity:
Understanding the time and space complexity of your solution is important for writing more efficient algorithms.
- [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

### Recursion:
Some solutions might require a recursive approach to traverse through the boxes and keys.
- [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

### Queue and Stack:
Knowing how to use queues and stacks is crucial for implementing BFS or DFS algorithms to traverse through the keys and boxes.
- [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)

### Set Operations:
Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.
- [Python Sets (Python Official Documentation)](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

## Additional Resources
- Mock Technical Interview

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3 (version 3.4.3)`
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should be documented
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Task

### Lockboxes

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to other boxes.

Write a method that determines if all the boxes can be opened.

#### Prototype: 
```python
def canUnlockAll(boxes)
