#!/usr/bin/python3
"""
Module to determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened

    Args:
        boxes (list of list of int): List of lists where each sublist contains keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked_boxes = set([0])
    keys = set(boxes[0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                stack.append(key)
                keys.update(boxes[key])

    return len(unlocked_boxes) == n
