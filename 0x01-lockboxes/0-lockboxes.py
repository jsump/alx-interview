#!/usr/bin/python3
"""
Module: 0-lockboxes.py

This module contains a function that determines if all boxes
are opened
"""


def canUnlockAll(boxes):
    """
    this function determines if all boxes can be opened

    boxes: lists of lists
    A key with the sae number as box opens that box
    Assume all keys will be positive numbers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True is al boxes can be opened, else return False
    """
    if not boxes:
        return False

    total_boxes = len(boxes)
    unlocked_boxes = [False] * total_boxes
    unlocked_boxes[0] = True

    for current_box in range(total_boxes):
        if not unlocked_boxes[current_box]:
            continue

        keys = boxes[current_box]
        for key in keys:
            if key < total_boxes:
                unlocked_boxes[key] = True

    return all(unlocked_boxes)
