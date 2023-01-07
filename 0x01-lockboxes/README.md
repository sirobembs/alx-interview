0x01. Lockboxes

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False


This solution uses a set to store the keys that have been seen so far, and a set to store the boxes that need to be checked. It first adds the keys from the first box to the set of seen keys and the set of boxes to check. It then iteratively checks boxes and adds their keys to the set of seen keys, and adds any boxes that can be unlocked with the new keys to the set of boxes to check. It stops when there are no more boxes to check, and returns whether all boxes have been seen.

