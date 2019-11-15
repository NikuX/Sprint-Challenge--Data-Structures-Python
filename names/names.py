import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# # option 1 = 8.4sec
# duplicates = []
# for name_1 in names_1:  # 0(n^2)
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# # option 2 = 1.46sec
# duplicates = []
# for name in names_1:    # O(n)
#     if name in names_2:
#         duplicates.append(name)

'''option 3 = 0.12 sec'''
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)




    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        else:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

bst = BinarySearchTree(names_1[0])

duplicates = []

for name in names_1:
    bst.insert(name)

for name in names_2:  # O(n log(n))
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

