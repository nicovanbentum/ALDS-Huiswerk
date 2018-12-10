


class hash_map:
    def __init__(self, size):
        self.table = list(size)

    def __repr__(self):
        return str(self.table)

    def insert(self, e):
        i = e % 10

        if i

        

        if self.table[i]:
            self.table[i].add(e)
        else:
            self.table[i] = set()
            self.table[i].add(e)


test_map = hash_map()
test_map.insert(45)
test_map.insert(12)

print(test_map)