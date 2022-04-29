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
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def __len__(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length


    def __str__(self):
        current = self.head
        while current.next is not None:
            print(" {}".format(current.data), end="")
            current = current.next

        print(" {}".format(current.data), end="")
        current = current.next
        return ""


    def __iter__(self):
        return LinkedListIterator(self.head)

    
    def get(self, idx):
        current = self.head
        i = 0
        while current is not None:
            if i == idx:
                return current.data 
            current = current.next
            i += 1
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
        node = Node(data=data)

        if id == 0:
            switched_node = self.head
            self.head = node
            node.next = switched_node
            switched_node.prev = node
            return 
        
        current = self.head
        count = 1
        while count < id:
            if count == len(self):
                current.next = node
                node.prev = current
                return 
            current = current.next
            count += 1
        switched_node = current.next

        switched_node.prev = node
        node.next = switched_node

        current.next = node
        node.prev = current


    def shift(self):
        if self.head is None:
            return 
        next = self.head.next
        self.head.next = None
        next.prev = None
        self.head = next


    def pop(self):
        if self.head is None:
            print("Лист пустий")
            return 
        
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
        if self.head is None:
            return True
        return False
 
