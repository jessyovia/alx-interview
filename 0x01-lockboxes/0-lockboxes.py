#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    unlocked_boxes = set()
    unlocked_boxes.add(0)
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

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
