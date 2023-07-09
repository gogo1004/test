import sys

with open("SMF.txt", "r") as f:
    for line in f:
        for char in line:
            if char == "\t":
                print("Tab")
            else:
                print("Space")