from os import stat
from .DoublyLinkedList import LinkedList

class Graph:
    def __init__(self, num_nodes, directed=False):
        self.num_nodes = num_nodes
        self.vertexes = LinkedList()
        self.directed = directed
        # weighted & weights:
        self.weighted = False
        self.weights = LinkedList.get_matrix(num_nodes)
        # edges: 
        self.data = LinkedList.get_matrix(num_nodes)
        # визначає, чи є граф орієнтованим

    def __repr__(self):
        string = ""
        for idx_node, neighbours in enumerate(self.data):
            string += f"{self.vertexes[idx_node]}:" +\
                f"{list(self.vertexes[i] for i in neighbours)}\n"
        return string

    def print_weights(self):
        string = ""
        for idx_node, weights in enumerate(self.weights):
            string += f"{self.vertexes[idx_node]}:" +\
                    f"{weights}\n"
        print(string)

    def addVertex(self, vertex):
        self.vertexes.append(vertex)

    def addEdge(self, edge):
        weighted = len(edge) == 3
        if weighted:
            n1, n2, weight = edge
            self.weights[n1].append(weight)
            self.weighted = True
        else:
            n1, n2 = edge
        self.data[n1].append(n2)
            
        if not self.directed:
            self.data[n2].append(n1)
            if weighted:
                self.weights[n2].append(weight)

    def delete_connection(self, v1, v2):
        # проходимося по кожній сусідній вершині v1 
        for i, vertex in enumerate(self.data[v1]):
            # якщо поточна сусідн. верш. дорівнює v2
            if vertex == v2:
                # видалити сусіда v1, відповідно видалити вагу
                self.data[v1].remove(v2)
                weight = self.weights[v1][i]
                self.weights[v1].remove(weight)
        # якщо більше немає з'єднань - видалити її з листа вершин
        if len(self.data[v1]) == 0:
            self.vertexes.remove(v1)

    def delete_edge(self, v1, v2):
        self.delete_connection(v1, v2)
        if not self.directed:
            self.delete_connection(v2, v1)

    def bfs(self, root=0):
        result = LinkedList()
        queue = LinkedList()
        passed = [False] * len(self.data)

        # додавання поточної вершини у чергу,
        # відмічання, що вона буда пройдена 
        passed[root] = True
        queue.append(root)
        
        while len(queue) > 0:
            # взяття першої вершини зі стеку
            v = queue.shift()
            result.append(self.vertexes[v])
            # додавання в чергу усіх сусідніх
            # вершин, які не були пройдені
            for node in self.data[v]:
                if not passed[node]:
                    passed[node] = True
                    queue.append(node)
        return result

    def dfs(self, root=0):
        result = LinkedList()
        stack = LinkedList()
        passed = [False] * len(self.data)

        #додаємо передану вершину в стек
        stack.append(root)

        while len(stack) > 0:
            v = stack.pop()

            if not passed[v]:
                result.append(self.vertexes[v])
                passed[v] = True
                for n in self.data[v]:
                    if not passed[n]:
                        stack.append(n)
        return result

    def update_distances(self, current, distance):
        neighbours = self.data[current]
        weights = self.weights[current]

        for i, node in enumerate(neighbours):
            weight = weights[i]
            if distance[current] + weight < distance[node]:
                distance[node] = distance[current] + weight

    def pick_next_node(self, distance, visited):
        min_distance = float('inf')
        min_node = None
        for node in range(len(distance)):
            if not visited[node] and distance[node] < min_distance:
                min_node = node
                min_distance = distance[node]
        return min_node
    
    # Dijkstra’s Shortest Path Algorithm
    def shortest_path(self, source, target):
        visited = [False] * self.num_nodes
        distance = [float('inf')] * self.num_nodes
        queue = []

        distance[source] = 0
        queue.append(source)
        idx = 0

        while idx < len(queue) and not visited[target]:
            current = queue[idx]
            visited[current] = True
            idx += 1

            # оновити затримку (дистанцію) усіх сусідніх верш.
            self.update_distances(current, distance)

            # знайти першу невідвідану вершину з найменшою затримкою
            next_node = self.pick_next_node(distance, visited)
            if next_node:
                queue.append(next_node)

        return distance[target]

    def all_shortests_paths(self, source):
        for i in range(self.num_nodes):
            print(f"Затримка з {self.vertexes[source]} до {self.vertexes[i]} - {round(self.shortest_path(source, i), 2)}")

