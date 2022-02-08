import sys
import math

# Game Loop
while True:
    # Initial State each run
    highest = -1
    highest_index = -1

    # Iterate over mountain heights
    for i in range(8):
        mountain_h = int(input())
        
        # If greater then record height and mountain index
        if mountain_h > highest:
            highest = mountain_h
            highest_index = i

    print(highest_index)