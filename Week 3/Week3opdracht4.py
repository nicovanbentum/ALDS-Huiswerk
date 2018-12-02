import csv
import os

"""
METHODE 1
"""
def file2dict(filename):

    dict_to_return = {}

    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                if word in dict_to_return:
                    val = dict_to_return[word]
                    dict_to_return[word] = val+1
                else:
                    dict_to_return[word] = 1

    return dict_to_return

final_dict = file2dict('tekst.txt')
print(final_dict)

def write2csv(fDict, filename): #n is hoe vaak het woord voorkomt
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for w in fDict:
            value = fDict.get(w)
            writer.writerow([w, value])

os.remove('woorden.csv')
write2csv(final_dict, 'woorden.csv')

"""
METHODE 2
"""

class node():
    def __init__(self):
        self.children = {} #format key:value, characters:node
        self.n = 0


class Trie():
    def __init__(self):
        self.root = node()

    def insert(self, string):
        it = self.root
        key = ''

        for char in string:
            key += char
            if key in it.children:
                it = it.children[key]
            else:
                it.children[key] = node()
                it = it.children[key]
        it.n += 1

    def search(self, word):
        it = self.root
        key = ''
        for char in word:
            key += char
            if key in it.children:
                it = it.children[key]
            else:
                print("word not in Trie")
                return False
        return it.n


def file2trie(filename, trie):
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                trie.insert(word)

def trie2csv(filename, trie, node = None, word = ''):
    if node == None:
        node = trie.root

    if node.n > 0:
        with open(filename, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow([word, node.n])

    for e in node.children:
        word = e
        trie2csv(filename, trie, node.children[e], word)



t = Trie()
file2trie('tekst.txt', t)

os.remove('woorden_trie.csv')
trie2csv('woorden_trie.csv', t)

print("SEE CSV FILES (AND THE ORIGINAL TEXT FILE) FOR RESULTS")