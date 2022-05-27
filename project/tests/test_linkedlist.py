import unittest
from DataStructures.DoublyLinkedList import LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()
        self.list2 = LinkedList()
        for i in range(10):
            self.list2.append(i)

    def test_append(self):
        for i in range(10):
            self.list.append(i)
            self.assertEqual(self.list[i], i)

    def test_insert(self):
        for i in range(10):
            self.list.insert(i, i+1)
            self.assertEqual(self.list[i], i+1)

    def test_setitem(self):
        for i in range(10):
            self.list.append(0)
            self.list[i] = i+1
            self.assertEqual(self.list[i], i+1)

    def test_get_by_id(self):
        for i in range(10):
            self.list._get_by_id(i) == i

    def test_unshift(self):
        li = LinkedList()
        self.list2.unshift(10)
        li.unshift(0)
        self.assertEqual(li[0], 0)
        self.assertEqual(self.list2[0], 10)
        self.assertEqual(self.list2[1], 0)

    def test_is_empty(self):
        self.assertEqual(self.list.is_empty(), True)
        self.list.append(1)
        self.assertEqual(self.list.is_empty(), False)

    def test_get_matrix(self):
        matrix = LinkedList.get_matrix(10, 5)
        for i in range(10):
            for j in range(5):
                self.assertEqual(matrix[i][j], 0)


if __name__ == '__main__':
    unittest.main()