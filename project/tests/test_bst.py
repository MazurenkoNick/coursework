import unittest
from DataStructures.BinaryTree import BSTNode


class BSTTests(unittest.TestCase):
    def setUp(self):
        self.tree = BSTNode('5.5.5.5', 'Nick')
        self.tree.insert('1.1.1.1', 'Ivan')
        self.tree.insert('2.2.2.2', 'Taras') 
        self.tree.insert('3.3.3.3', 'Kirill') 
        self.tree.insert('4.4.4.4', 'Petr') 

    def test_contains(self):
        self.assertEqual('1.1.1.1' in self.tree, True)
        self.assertEqual('1.1.1.2' in self.tree, False)

    def test_get(self):
        self.assertEqual(self.tree.get_by_key('1.1.1.1').value, 'Ivan')
        self.assertEqual(self.tree.get_by_key('2.2.2.2').value, 'Taras')
        self.assertEqual(self.tree.get_by_key('1.1.1.2'), None)

    def test_insert(self):
        self.tree.insert('6.6.6.6', 'Anny')
        self.assertEqual(self.tree.get_by_key('6.6.6.6').value, 'Anny')
        self.assertEqual(self.tree.size(), 6)

    def test_update(self):
        self.tree.update('5.5.5.5', 'Nikita')
        self.assertEqual(self.tree.get_by_key('5.5.5.5').value, 'Nikita')

        with self.assertRaises(KeyError):
            self.tree.update('1.1.1.2', 'Nikita')

    def test_height(self):
        self.assertEqual(self.tree.height(), 5)
        self.tree.insert('6.6.6.6', 'Anny')
        self.assertEqual(self.tree.height(), 5)

    def test_iterator(self):
        i = 1
        for node in self.tree:
            self.assertEqual(str(node), f"{i}.{i}.{i}.{i}")
            i+=1

    def test_contains(self):
        tree = BSTNode('1.1.1.1', '1')
        self.assertTrue('1.1.1.1' in tree)


if __name__ == '__main__':
    unittest.main()