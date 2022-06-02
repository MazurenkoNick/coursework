from DataStructures.Graph import Graph
from DataStructures.BinaryTree import BSTNode
from DataStructures.DoublyLinkedList import LinkedList
from csv import DictReader

edges = LinkedList()
vertexes = LinkedList()
bst = BSTNode('me', '0.0.0.0')
vertexes.append('0.0.0.0')

# додавання ребер у edges
with open("edges.csv") as f:
    file = DictReader(f)
    for edge in file:
        e = LinkedList()
        e.append(int(edge['vertex1']))
        e.append(int(edge['vertex2']))
        e.append(int(edge['weight']))
        edges.append(e)

# заповнення бінарного дерева та додавання вершин у vertexes
with open('IPs.csv') as f:
    file = DictReader(f)
    for row in file:
        dns = row['DNS']
        ips = LinkedList()
        for ip in row['IP'].split(','):
            ips.append(ip)

        bst.insert(dns, ips)
        for ip in ips:
            vertexes.append(ip)

print('DNS, IPs')
bst.print_all()

g1 = Graph(6, directed=False)

# додавання вершин і ребер у граф
for i in edges:
    g1.addEdge(i)
for v in vertexes:
    g1.addVertex(v)


print("IP Connections:")
print(g1)

print("BFS(0):", g1.bfs())
print("DFS(0):", g1.dfs())

print('\nDijkstra’s Shortest Path Algorithm:')
g1.all_shortests_paths(0)

print('\nAfter deleting edge (0,1):')
g1.delete_edge(0, 1)

print("IP Connections:")
print(g1)

print("BFS(0):", g1.bfs())
print("DFS(0):", g1.dfs())

print('\nDijkstra’s Shortest Path Algorithm:')
g1.all_shortests_paths(0)