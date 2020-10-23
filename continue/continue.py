"""

The continue statement, also borrowed from the C language, continues with the next loop iteration:
"""

for num in range(2, 10):
    if num %  2 == 0:
        print("Found an even number", num)
        continue

    print("Found an odd number", num)