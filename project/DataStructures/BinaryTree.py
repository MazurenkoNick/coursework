from .DoublyLinkedList import LinkedList


class TreeNodeIterator:
    def __init__(self, root_node):
        self.current = root_node
        self.stack = LinkedList()

        self._append_left_side()

    def __iter__(self):
        return self

    def __next__(self):
        # ініціалізуємо ноду листа, беручи її зі стаку
        list_node = self.stack.pop()
        if list_node is None:
            raise StopIteration
        
        # ініціалізуємо праву ноду BST 
        self.current = list_node.data.right

        # додаємо всі елементи поточної (правої) ноди до стаку
        self._append_left_side()
        
        return list_node.data

    def _append_left_side(self):
        while self.current is not None:
            self.stack.append(self.current)
            self.current = self.current.left


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __iter__(self):
        return TreeNodeIterator(self)

    def __repr__(self):
        return str(self.key)

    def __contains__(self,key):
        if self.get_by_key(key):
            return True
        else:
            return False

    def height(self):
        """
        function returns height of the tree
        """
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        """
        function returns size of the tree
        """
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)
    
    def get_by_key(self, key):
        """
        function finds and returns the node with a key,
        that's passed as an argument to the method
        """
        # якщо дерево пусте - повернути None
        if self is None:
            return None

        # знайшли відповідний ключ, повертаємо ноду.
        elif key == self.key:
            return self

        # пройти до потрібного місця рекурсивним шляхом.
        elif self.key > key:
            return TreeNode.get_by_key(self.left, key)
        elif self.key < key:
            return TreeNode.get_by_key(self.right, key)

    def delete(self, key):
        pass
        


class BSTNode(TreeNode):
    def __init__(self, key, value=None):
        super().__init__(key)
        self.value = value
        self.parent = None

    def insert(self, key, value):
        """
        function creates and inserts new BSTNode into 
        the tree using key-value pair, that's passed
        to the method as arguments
        """
        # дійшли до пустого вузла, ініціалізуємо його 
        if self is None:
            self = BSTNode(key, value)
        
        # пройти до потрібного місця рекурсивним шляхом.
        elif self.key < key:
            self.right = BSTNode.insert(self.right, key, value)
            self.right.parent = self

        elif self.key > key:
            self.left = BSTNode.insert(self.left, key, value)
            self.left.parent = self
        return self


    def update(self, key, value):
        """
        function updates the value of the node with a key,
        that's passed as an argument to the method. value is passed as 
        the second argument
        """
        node = self.get_by_key(key)
        if node is not None:
            node.value = value
        else:
            raise KeyError
