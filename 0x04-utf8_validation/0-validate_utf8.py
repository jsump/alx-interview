#!/usr/bin/python3
"""
Module: 0-validate_utf8.py

This module contains a function that determines if a given
dataset represents UTF-8 encoding
"""


def validUTF8(data):
    """
    This method determines whether a given dataset represents
    a valid UTF-8 encoding

    Dataset can have multiple characters
    Dataset will be represented by a list of integers

    Return: True if data is a valid UTF-8 encoding, else return False
    """
    num_bytes = 0

    # Mask to check if the first and second most significant bit are set
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Check if number of bytes is 0, meaning a new character
        if num_bytes == 0:
            for bit in range(7, -1, -1):
                if (num & (1 << bit)) == 0:
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1
    return num_bytes == 0
