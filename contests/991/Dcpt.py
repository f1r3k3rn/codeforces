import sys
from collections import defaultdict

input = sys.stdin.readline

def inp():
    return int(input())

def insr():
    s = input()
    return list(s.strip())

class Node:
    """Nodo di una lista doppiamente collegata."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """Lista doppiamente collegata."""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Aggiunge un nodo alla fine della lista."""
        new_node = Node(data)
        if not self.head:  # Lista vuota
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_before(self, ref_node, data):
        """Inserisce un nodo prima di un nodo di riferimento."""
        new_node = Node(data)
        if ref_node.prev:
            ref_node.prev.next = new_node
            new_node.prev = ref_node.prev
        else:  # Se il nodo di riferimento è la testa
            self.head = new_node
        new_node.next = ref_node
        ref_node.prev = new_node

    def delete(self, node):
        """Rimuove un nodo dalla lista."""
        if node.prev:
            node.prev.next = node.next
        else:  # Nodo è la testa
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:  # Nodo è la coda
            self.tail = node.prev

    def to_list(self):
        """Converte la lista doppiamente collegata in una lista Python."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    @classmethod
    def from_list(cls, lst):
        """Crea una lista doppiamente collegata da una lista Python."""
        dll = cls()
        for item in lst:
            dll.append(item)
        return dll

def solve(vet):
    dll = DoublyLinkedList.from_list(list(map(int, vet)))
    current = dll.head

    while current:
        mas = 0
        k_node = None
        temp = current.next
        j = 1

        while temp and j < 9:
            if temp.data - j > mas:
                mas = temp.data - j
                k_node = temp
            temp = temp.next
            j += 1

        if mas > current.data and k_node:
            dll.delete(k_node)
            dll.insert_before(current, mas)
        else:
            current = current.next


    return "".join(map(str, dll.to_list()))

def main():
    t = inp()
    outs = []
    for _ in range(t):
        s = insr()
        outs.append(solve(s))

    print("\n".join(outs))

if __name__ == "__main__":
    main()
