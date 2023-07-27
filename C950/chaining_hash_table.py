# hash table objects will have space complexities of O(n)
class chaining_hash_table:
    def __init__(self, init_capacity=10):

        self.table = []
        for i in range(init_capacity):
            self.table.append([])

    def __call__(self):
        for x in self.table:
            print(x)

    # Insert items into hash table. If entry is already present at that key it updates the value. O(1)
    def insert(self, key, item):
        packageIndex = hash(key) % len(self.table)
        chain = self.table[packageIndex]
        key_value = [key, item]
        for kv in chain:
            if (kv[0] == key):
                kv[1] = item
                return True

        chain.append(key_value)
        return True

    # Removes an item from an existing hash table. O(1)
    def remove(self, key):
        packageIndex = hash(key) % len(self.table)
        chain = self.table[packageIndex]

        for kv in chain:
            if (kv[0] == key):
                chain.remove([kv[0],kv[1]])
            else:
                print("No package with that ID was found in the truck.")

    # Searches for an entry in a hash table based on a provided key. O(1)
    def lookup(self, key):
        packageIndex = hash(key) % len(self.table)
        chain = self.table[packageIndex]
        for kv in chain:
            if kv[0] == key:
                return kv[1]
        return None
