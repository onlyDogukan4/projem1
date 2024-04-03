from collections import Counter

keys = []
keys2 = []
keys3 = []
keys4 = []

file = "Words.txt"
with open(file, "r") as dosya:
    for satır in dosya:
        kelimeler = satır.split()
        for kelime in kelimeler:
            lower_kelime = kelime.lower()
            keys.append(lower_kelime)
            keys2.append(lower_kelime)
            keys3.append(lower_kelime)
            keys4.append(lower_kelime)

print("----Homework First Condition-----")
def kelime_sayilari(keys3):
    sayilar = Counter(keys3)
    for kelime in keys3:
        print(f"{kelime}: {sayilar[kelime]} adet")

kelime_sayilari(keys3)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.count = 1

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key == root.key:
            root.count += 1
        if key < root.key:
            root.left = insert(root.left, key)
        elif key > root.key:
            root.right = insert(root.right, key)
    return root

root = None

for key in keys:
    root = insert(root, key)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(f"{node.key}: {node.count} times ")
        in_order_traversal(node.right)

print("----- HomeWork Second Condition: -----")
in_order_traversal(root)

print("----- HomeWork Third Condition: -----")

search_word = input("Enter a word to search: ").lower()
search_depth = search(root, search_word)
