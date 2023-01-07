#!/usr/bin/python3

"""Exercise to practice interview"""


def canUnlockAll(boxes):
    """Set to store the keys we have seen so far"""
    seen = set()
    """Add the keys from the first box to the set"""
    seen.update(boxes[0])
    """Set of boxes we need to check"""
    to_check = seen.copy()

    """Keep checking boxes while there are boxes to check"""
    while to_check:
        """Take a box to check"""
        box = to_check.pop()
        """Add its keys to the set of seen keys"""
        seen.update(boxes[box])
        """Add the boxes that can be unlocked with the new keys to the set of boxes to check"""
        to_check.update(set(boxes[box]) - seen)

    """Return whether all boxes have been seen"""
    return len(seen) == len(boxes)
