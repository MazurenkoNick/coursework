class Node:
    def __init__(self, next=None, prev=None, data=None):
        # посилання на наступну ноду
        self.next = next 
        # посилання на минулу ноду
        self.prev = prev
        self.data = data

    def __str__(self):
        return str(self.data)


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        # умова виходу з ітерації
        if self.current is None:
            raise StopIteration
        else:
            item = self.current
            self.current = self.current.next
            return item


class LinkedList:
    def __init__(self):
        self.head = None


    def __len__(self):
        current = self.head
        length = 0
        # ітеруємо та інкрементуємо length,
        # поки перетнемо останній елемент
        while current is not None:
            length += 1
            current = current.next
        return length


    def __str__(self):
        current = self.head
        string = '['
        if len(self) > 1:
            while current.next is not None:
                string += "{}, ".format(current.data)
                current = current.next

            string += "{}]".format(current.data)
        return string


    def __iter__(self):
        return LinkedListIterator(self.head)
    

    def __setitem__(self, id, data):
        node = self._get_by_id(id)
        if node is not None:
            node.data = data
        else:
            raise IndexError


    def __getitem__(self, id):
        node = self._get_by_id(id)
        return node.data if node else None


    def __add__(self, other):
        if isinstance(other, LinkedList):
            list = LinkedList()
            for node in self:
                list.append(node.data)
            for node in other:
                list.append(node.data)
            return list
        return "Can't concatenate these two objects"

    
    def __contains__(self, value):
        if self.head is None:
            return False
        
        current = self.head

        while current is not None: 
            if current.data == value:
                return True
            current = current.next
        return False

    
    def _get_by_id(self, idx):
        """
        function returns element under the given index 
        """
        current = self.head
        i = 0

        # ітеруємо поки не досягнемо кінцевого елементу
        while current is not None:
            if i == idx:
                return current
            current = current.next
            i += 1

        # індекс виходить за межі останнього індексу листа
        return None


    def unshift(self, data):
        """
        function adds Node with data, that's passed as an
        argumnet, to the beginning of the list
        """
        # ініціалізуємо ноду
        node = Node(data=data)

        # визначаємо наступну ноду та минулу 
        node.next = self.head
        node.prev = None

        # змінюємо минулу ноду в head node на теперішню
        if self.head is not None:
            self.head.prev = node

        # змінюємо head node вказівник на теперішню
        self.head = node

    
    def append(self, data):
        """
        function adds Node with data, that's passed as an
        argumnet, to the end of the list
        """
        node = Node(data=data)
        current = self.head

        # якщо head - None, то масив пустий
        # ініціалізуємо self.head
        if current is None:
            self.head = node
            return 
        
        # йдемо до останнього елементу листа
        while current.next is not None:
            current = current.next

        current.next = node
        node.prev = current


    def insert(self, id, data):
        """
        function inserts Node in the given index,
        moving forward the previous element under this id
        """
        node = Node(data=data)

        if id == 0:
            switched_node = self.head
            self.head = node
            node.next = switched_node
            # перевіряємо щоб попередній head node не був None
            if switched_node is not None:
                switched_node.prev = node
            return 

        # якщо id виходить за межі довжини листа,
        # то додаємо елемент у кінець
        if id >= len(self):
            self.append(data)
            return 

        prev = None
        current = self.head
        count = 0

        # ітеруємо поки не досягнемо id-1 
        while count < id:
            prev = current
            current = current.next
            count += 1
        
        # робимо switch ноди
        current.prev = node
        node.next = current
        prev.next = node
        node.prev = prev


    def shift(self):
        """
        function deletes the first node of the list
        """
        if self.head is None or len(self) == 1:
            return self.pop()
        
        next = self.head.next
        self.head.next = None
        next.prev = None
        self.head = next


    def pop(self):
        """
        function deletes and returns the last element of the list
        """
        if self.head is None:
            return None

        if len(self) == 1:
            node = self.head
            self.head = None
            return node
        
        current = self.head
        
        # шукаємо останній елемент у листі
        while current.next is not None:
            current = current.next

        # видаляємо останній елемент, видаляючи
        # зв'язки між останньою та передостанньою нодою
        prev_node = current.prev
        prev_node.next = None
        current.prev = None
        return current


    def is_empty(self):
        """
        function checks if the list is empty
        """
        if self.head is None:
            return True
        return False
