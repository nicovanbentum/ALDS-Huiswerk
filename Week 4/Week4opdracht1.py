
import random

class hash_map:
    def __init__(self, size):
        self.table = list()
        self.table = [None] * size
        self.size = size
        self.load_factor = 0

    def __repr__(self):
        return str(self.table)

    def insert(self, e):
        i = e % self.size
        if self.table[i]:
            self.table[i].add(e)
        else:
            self.table[i] = set()
            self.table[i].add(e)

        self.load_factor = self.total_elements() / self.size
        if self.load_factor > 0.75:
            self.rehash()
            print(self.table)

    def search(self, e):
        i = e % self.size
        if self.table[i]:
            for element in self.table[i]:
                if element == e:
                    return True
        return False
    
    def delete(self, e):
        i = e % self.size
        if (self.table[i]) and (e in self.table[i]):
            self.table[i].remove(e)
        self.load_factor = self.total_elements() / self.size

    def total_elements(self):
        total_elements = 0
        for _set in self.table:
            if _set:
                for e in _set:
                    total_elements += 1
        return total_elements

    def rehash(self): #doubles the size of the table
        temp_table = self.table.copy()
        self.size = self.size*2
        self.table = [None] * (self.size)

        for _set in temp_table:
            if _set:
                for e in _set:
                    self.insert(e)


##### TEST #####
test_map = hash_map(2)
print(test_map)

for _ in range(200): #maak deze getallen kleiner voor leesbare output
    random_number = random.randint(0, 5000)
    test_map.insert(random_number)

for _ in range(100): #maak deze getallen kleiner voor leesbare output
    random_number = random.randint(0, 5000)
    test_map.delete(random_number)

print("-------------")
print(test_map)
