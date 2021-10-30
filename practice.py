treeRows = int(input("Enter how many rows your tree should be: "))

spaces = treeRows -1
hashes = 1
stump = treeRows -1

while treeRows != 0:
    for i in range(spaces):
        print(' ',end = '')
    for i in range(hashes):
        print('#', end = '')
    print()

    spaces -= 1
    hashes += 2
    treeRows -= 1

for i in range(stump):
    print(' ', end = '')

print('#')
