from DataStructures.Graph import Graph
from DataStructures.BinaryTree import BSTNode
from DataStructures.DoublyLinkedList import LinkedList
from csv import DictReader

edges = LinkedList() # ребра - використовується в графі. лист з вершинами і вагами [[0,1,36], [0,5,12], ...] з edge.csv файлу
vertexes = LinkedList() # ребра - використовується в графі. вершини - [me, 1.1.1.1, 2.2.2.2, 3.3.3.3, 4.4.4.4, 5.5.5.5]
bst = BSTNode() # бінарне дерево для виведення таблиці з іменами та відповідними ip адресами (ключ - ім'я, значення - список id)

# додавання ребер у edges
with open("edges.csv") as f: 
    file = DictReader(f)
    for edge in file: # прохід по кожному рядку файлу
        e = LinkedList() # створення ребра 
        e.append(int(edge['vertex1']))
        e.append(int(edge['vertex2']))
        e.append(int(edge['weight']))
        edges.append(e)

# заповнення бінарного дерева та додавання вершин у vertexes
with open('IPs.csv') as f:
    file = DictReader(f)
    for row in file: # прохід по кожній строчці у файлі IPs.csv
        dns = row['DNS']
        ips = LinkedList() # [1.1.1.1, 2.2.2.2]
        for ip in row['IP'].split(','):
            ips.append(ip) # заповнення списку з ip адресами поточного dns

        bst.insert(dns, ips) # додавання dns та листа з IPшніками в бінарне дерево пошуку

        for ip in ips:
            vertexes.append(ip) # додавання в вершини IP 

print('DNS, IPs')
bst.print_all() # виведення бінарного дерева

g1 = Graph(6, directed=False) # створення графа

# додавання вершин і ребер у граф
for i in edges:
    g1.addEdge(i)
for v in vertexes:
    g1.addVertex(v)

print("IP Connections:")
print(g1)

print("BFS(0):", g1.bfs()) # прохід в ширину
print("DFS(0):", g1.dfs()) # прохід в глибину

print('\nDijkstra’s Shortest Path Algorithm:')
g1.all_shortests_paths(0)

print('\nAfter deleting edge (0,1):')
g1.delete_edge(0, 1) # емуляція розірвання зв'язків між вершинами

print("IP Connections:")
print(g1)

print("BFS(0):", g1.bfs())
print("DFS(0):", g1.dfs())

print('\nDijkstra’s Shortest Path Algorithm:')
g1.all_shortests_paths(0)