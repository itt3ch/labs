import unittest

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

class TestBinaryTreeQueue(unittest.TestCase):
    def setUp(self):
        self.binary = BinaryTreeQueue()

    def test_insert(self):
        self.binary.insert("Task 1", 5)
        self.assertEqual(self.binary.highest(), "Task 1")
        self.binary.insert("Task 2", 3)
        self.assertEqual(self.binary.highest(), "Task 1")
        self.binary.insert("Task 3", 8)
        self.assertEqual(self.binary.highest(), "Task 3")
        self.binary.insert("Task 4", 1)
        self.assertEqual(self.binary.highest(), "Task 3")

    def test_delete(self):
        self.binary.insert("Task 1", 5)
        self.binary.insert("Task 2", 3)
        self.binary.insert("Task 3", 8)
        self.binary.insert("Task 4", 1)
        self.assertEqual(self.binary.delete(), "Task 3")
        self.assertEqual(self.binary.delete(), "Task 1")
        self.assertEqual(self.binary.delete(), "Task 2")
        self.assertEqual(self.binary.delete(), "Task 4")
        self.assertIsNone(self.binary.delete())

    def test_highest(self):
        self.assertIsNone(self.binary.highest())
        self.binary.insert("Task 1", 5)
        self.assertEqual(self.binary.highest(), "Task 1")
        self.binary.insert("Task 2", 3)
        self.assertEqual(self.binary.highest(), "Task 1")
        self.binary.insert("Task 3", 8)
        self.assertEqual(self.binary.highest(), "Task 3")
        self.binary.insert("Task 4", 1)
        self.assertEqual(self.binary.highest(), "Task 3")

if __name__ == "__main__":
    unittest.main()
