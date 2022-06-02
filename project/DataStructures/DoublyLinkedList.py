class Node:
    def __init__(self, next=None, prev=None, data=None):
        # посилання на наступну вершину
        self.next = next 
        # посилання на минулу вершину
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
            return item.data


class LinkedList:
    def __init__(self):
        self.head = None


    def __len__(self):
        current = self.head
        length = 0
        # ітеруємо та інкрементуємо length,
        # поки перетнемо останній елемент
        while current:
            length += 1
            current = current.next
        return length


    def __str__(self):
        current = self.head
        string = '['
        if len(self) >= 1:
            if not isinstance(current.data, LinkedList):
                # додати всі елементи до строки 
                while current.next:
                    string += f"{current.data}, "
                    current = current.next
                string += f"{current.data}"

            # якщо лист містить інші листи (матриця)
            else:
                # додати всі елементи до строки 
                while current.next:
                    string += current.data.__str__()
                    string += ",\n "
                    current = current.next
                string += current.data.__str__()

        string += "]"
        return string


    def __iter__(self):
        return LinkedListIterator(self.head)
    

    def __setitem__(self, id, data):
        node = self._get_by_id(id)
        if node:
            node.data = data
        else:
            raise IndexError


    def __getitem__(self, id):
        node = self._get_by_id(id)
        return node.data if node else None


    def __add__(self, other):
        """concatenate two lists"""
        if isinstance(other, LinkedList):
            list = LinkedList()
            # додаємо всі елементи поточного листа
            for node in self:
                list.append(node.data)
            # додаємо всі елементи іншого листа
            for node in other:
                list.append(node.data)
            return list
        return "Can't concatenate these two objects"

    
    def __contains__(self, value):
        # якщо лист пустий
        if self.is_empty():
            return False
        
        current = self.head
        
        # ітеруємо поки не знайдемо відповідний елемент,
        # або, поки не проітеруємо весь лист
        while current: 
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
        while current:
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
        # ініціалізуємо вершину
        node = Node(data=data)

        # визначаємо наступну вершину та минулу 
        node.next = self.head
        node.prev = None

        # змінюємо минулу вершину в head node на теперішню
        if self.head:
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
        while current.next:
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
            if switched_node:
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
        
        node = self.head

        next_node = self.head.next
        self.head.next = None
        next_node.prev = None
        self.head = next_node

        return node.data


    def pop(self, idx=None):
        """
        function deletes and returns the last element of the list
        """
        if self.head is None:
            return None

        if len(self) == 1:
            node = self.head
            self.head = None
            return node.data
        
        current = self.head
        
        # шукаємо останній елемент у листі
        while current.next:
            current = current.next

        # видаляємо останній елемент, видаляючи
        # зв'язки між останньою та передостанньою нодою
        prev_node = current.prev
        prev_node.next = None
        current.prev = None
        return current.data

    def remove(self, value):
        current = self.head

        # якщо лист пустий - повернути None
        if self.is_empty(): 
            return None

        # якщо значення першого елементу й 
        # значення аргументу збіглись - викликати shift()
        if self.head.data == value:
            return self.shift()
        
        # пройтись по кожному елементу листа, окрім останнього,
        # перевірити на рівність значення з аргументу й листа,
        # видалити при збіжності, ні - продовжити ітерацію
        while current.next:
            if current.data == value:
                next_node = current.next
                prev_node = current.prev
                next_node.prev = prev_node
                prev_node.next = next_node
                return
            current = current.next
        
        # якщо значення останнього елемента дорівнює значенню
        # аргумента - викликати метод pop() 
        if current.data == value: 
            return self.pop()

        print('Element wasn\'t found')
        print(self)
        return None

    def is_empty(self):
        """
        function checks if the list is empty
        """
        if self.head is None:
            return True
        return False

    @staticmethod
    def get_matrix(len_rows, len_columns=0):
        list = LinkedList()
        for i in range(len_rows):
            row = LinkedList()
            for j in range(len_columns):
                row.unshift(0)
                
            list.append(row)
        return list

    @staticmethod
    def get_array(length):
        list = LinkedList()
        for i in range(length):
            list.unshift(0)
        return list
