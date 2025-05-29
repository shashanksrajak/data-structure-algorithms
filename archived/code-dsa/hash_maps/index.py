# Hash Maps

# Hash Maps are a data structure that store key-value pairs. They are similar to arrays, but the keys are not ordered. The keys are unique, and the values can be any data type. Hash maps are efficient for finding and storing data.

# Hash maps are implemented using an array. Each element in the array is a key-value pair. The key is used to calculate the index in the array where the value is stored. This is done using a hash function.


# Hash Functions
class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
