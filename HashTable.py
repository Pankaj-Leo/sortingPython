class HashTable:
    # Entry class to hold key-value pairs
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity=10):
        self.table = [None] * capacity  # Array of linked lists
        self.size = 0
        self.capacity = capacity

    def _hash(self, key):
        """Hash function to calculate index."""
        return abs(hash(key)) % self.capacity

    def put(self, key, value):
        """Put key-value pair into the hash table."""
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []  # Initialize a new bucket (linked list)
        # Check if key already exists and update it
        for entry in self.table[index]:
            if entry.key == key:
                entry.value = value  # Update the existing key
                return
        # Add new entry
        self.table[index].append(self.Entry(key, value))
        self.size += 1

    def get(self, key):
        """Get value by key."""
        index = self._hash(key)
        if self.table[index] is not None:
            for entry in self.table[index]:
                if entry.key == key:
                    return entry.value
        return None  # Key not found

    def remove(self, key):
        """Remove key-value pair."""
        index = self._hash(key)
        if self.table[index] is not None:
            for i, entry in enumerate(self.table[index]):
                if entry.key == key:
                    del self.table[index][i]  # Remove the entry
                    self.size -= 1
                    if len(self.table[index]) == 0:
                        self.table[index] = None
                    return

    def contains_key(self, key):
        """Check if the hash table contains a key."""
        return self.get(key) is not None

    def get_size(self):
        """Get the current size of the hash table."""
        return self.size

    def print_table(self):
        """Print all key-value pairs."""
        for i, bucket in enumerate(self.table):
            if bucket is not None:
                print(f"Index {i}: ", end="")
                for entry in bucket:
                    print(f"({entry.key}, {entry.value})", end=" ")
                print()

# Example usage
if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.put("one", 1)
    hash_table.put("two", 2)
    hash_table.put("three", 3)
    hash_table.print_table()

    print("Get 'two':", hash_table.get("two"))  # Output: 2
    hash_table.remove("two")
    print("Contains 'two':", hash_table.contains_key("two"))  # Output: False

    print("Size:", hash_table.get_size())  # Output: 2
    hash_table.print_table()