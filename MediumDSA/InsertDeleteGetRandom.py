import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}  # Dictionary to store value to index mapping
        self.val_list = []      # List to store values

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_list.append(val)
        self.val_to_index[val] = len(self.val_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last_val = self.val_list[-1]
        self.val_list[index], self.val_list[-1] = self.val_list[-1], self.val_list[index]
        self.val_to_index[last_val] = index
        del self.val_to_index[val]
        self.val_list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.val_list)


# Test case
commands = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
inputs = [[], [1], [2], [2], [], [1], [2], []]

randomizedSet = None
output = []

for command, values in zip(commands, inputs):
    if command == "RandomizedSet":
        randomizedSet = RandomizedSet()
        output.append(None)
    elif command == "insert":
        output.append(randomizedSet.insert(*values))
    elif command == "remove":
        output.append(randomizedSet.remove(*values))
    elif command == "getRandom":
        output.append(randomizedSet.getRandom())

print("Output:", output)
