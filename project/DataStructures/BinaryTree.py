from .DoublyLinkedList import LinkedList


class TreeNodeIterator:
    def __init__(self, root_node):
        self.current = root_node
        self.stack = LinkedList()

        self._append_left_side()

    def __iter__(self):
        return self

    def __next__(self):
        # ініціалізуємо вершину, беручи її зі стаку
        node = self.stack.pop()
        if node is None:
            raise StopIteration
        
        # ініціалізуємо праву вершину
        self.current = node.right

        # додаємо всі елементи поточної (правої) ноди до стаку
        self._append_left_side()
        
        return node

    def _append_left_side(self):
        """adds every left element of the current node to the stack"""
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left


class TreeNode:
    def __init__(self, key=None):
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

        # знайшли відповідний ключ, повертаємо вершину.
        elif key == self.key:
            return self

        # пройти до потрібного місця рекурсивним шляхом.
        elif self.key > key:
            return TreeNode.get_by_key(self.left, key)
        elif self.key < key:
            return TreeNode.get_by_key(self.right, key)


    def delete_node(self, key):
        """
        method deletes the node by the given key, except for the root node
        """
        if self is None:
            return None

        if self.key == key:
            # 4 відвітвлення:
            # якщо поточний елемент є листом, то просто видалити його
            if self.left is None and self.right is None:
                return None

            # якщо у видаленого елемента немає лівої сторони - повернути праву
            if self.left is None and self.right:
                return self.right

            # якщо у видаленого елемента немає правої сторони - повернути ліву
            if self.left and self.right is None:
                return self.left

            # якщо 2 дочірні існують:
            # знаходимо мінімальний елемент справа від видаленої
            # і його дані зміщуємо на місце видаленої ноди.
            # Видаляємо цей елемент з минулого місця.
            pointer = self.right
            while pointer.left:
                pointer = pointer.left
            self.key = pointer.key
            if isinstance(self, BSTNode):
                self.value = pointer.value
            self.right = TreeNode.delete_node(self.right, self.key)

        elif self.key > key:
            self.left = TreeNode.delete_node(self.left, key)
        else:
            self.right = TreeNode.delete_node(self.right, key)

        return self


    def display_keys(self, space='\t', level=0):    
        # якщо вершина пуста
        if self is None:
            print(space*level + '∅')
            return

        # якщо вершина - лист
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return
    
        # якщо вершина має дочірні вершини
        TreeNode.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display_keys(self.left,space, level+1)


class BSTNode(TreeNode):
    def __init__(self, key=None, value=None):
        super().__init__(key)
        self.value = value
        self.parent = None

    def print_all(self):
        string = ''
        for node in self:
            string += f'{node.key}: {node.value}\n'
        print(string)

    def insert(self, key, value=None):
        """
        function creates and inserts new BSTNode into 
        the tree using key-value pair, that's passed
        to the method as arguments
        """
        # дійшли до пустого вузла, ініціалізуємо його 
        if self is None:
            self = BSTNode(key, value)
        
        # BSTNode - пуста. Заповнити поля вершини
        elif self.key is None:
            self.key = key
            self.value = value
        
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
        if node:
            node.value = value
        else:
            raise KeyError
