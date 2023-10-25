"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items)):
        items[i] = str(items[i])

    for item in items:
        frequency = items.count(item)
        item = str(item)
        frequencies[item] = frequency
        
    return frequencies

