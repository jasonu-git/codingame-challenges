import sys
import math

n = 8

# Game Loop
while True:
    # Zip up inputs with indexes,
    # Get max pair using lambda expression comparing the mountain heights,
    # Print the index associated with the highest mountain.
    print(max(zip([int(input()) for _ in range(n)], range(n)), key=lambda x: x[0])[1])
    