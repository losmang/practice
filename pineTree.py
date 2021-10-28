# use 1 while loop and 3 for loops


# decrement spaces by 1 each time thorough the loop
# increment the hashes by 2 each time through the loop
# save spaces to the stump by calculating tree height -1
# decrement from tree height until it equals 0
# print stump spaces and then 1 hash

# get number of tree rows
treeRows = input("How many rows would you like your tree to have: ")

treeRows = int(treeRows)


# get starting spaces for the top of the tree
spaces = treeRows - 1


# there is one hash to start that will be incremented
hashes = 1

# save stump spaces till later
stump = treeRows - 1

# make sure the right number of rows are printed

while treeRows != 0:
    for i in range(spaces):
        print(' ', end = '')
    for i in range(hashes):
        print('#', end = '')
    print()

    spaces -= 1
    hashes +=2
    treeRows -= 1

for i in range(stump):
    print(' ',end = "")

print("#")
