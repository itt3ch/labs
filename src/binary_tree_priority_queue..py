class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class BinaryTreeQueue:
    def __init__(self):
        self.head = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.head:
            self.head = new_node
        elif self.head.priority < priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self):
        if not self.head:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            return value

    def highest(self):
        if self.head:
            return self.head.value
        else:
            return None

    def checkout(self):
        current = self.head
        while current:
            print(f"Value: {current.value}, Priority: {current.priority}")
            current = current.next

