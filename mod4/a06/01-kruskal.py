from collections import deque
from heapq import *

class DisjointSets:
    def __init__(self, size):
        self.dj = [i for i in range(size)]

    def find(self, elem):
        if self.dj[elem]!=elem:
            self.dj[elem] = self.find(self.dj[elem])
        return self.dj[elem]

    def union(self, elem1, elem2):
        self.dj[ self.find(elem1) ] = self.find(elem2)

class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [ [] for _ in range(V)]
        self.weight = [ [] for _ in range(V) ]

    def addEdge(self, u, v, w=1):
        self.adj[u].append(v)
        self.weight[u].append(w)
        self.E += 1

    def bfs(self, node):
        visited = set()
        visited.add(node)
        q = deque()
        q.append(node)
        while q:
            workingNode = q.popleft()
            for neigh in self.adj[workingNode]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append(neigh)

    def bfsList(self, node):
        visited = set()
        visited.add(node)
        q = deque()
        q.append(node)
        listOfVisitedNodes = []
        while q:
            workingNode = q.popleft()
            listOfVisitedNodes.append(workingNode)
            for neigh in self.adj[workingNode]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append(neigh)
        return listOfVisitedNodes

    def DijkstraWithoutHeap(self, source, target): # O(V^2+E)
        visited = [False]*self.V #O(V)

        dist = [float('inf')]*self.V #O(V)
        dist[source] = 0

        while True:  # O(V)
            workingNode = -1
            for i in range(self.V): #O(V^2)
                if visited[i]==False and (workingNode==-1 or dist[i]<dist[workingNode]):
                    workingNode = i
            if workingNode==-1:
                return float('inf')

            if workingNode==target:
                return dist[target]

            visited[workingNode] = True
            for index, neigh in enumerate(self.adj[workingNode]): #O(E)
                edgeWeight = self.weight[workingNode][index]
                if dist[workingNode] + edgeWeight < dist[neigh]:
                    dist[neigh] = dist[workingNode] + edgeWeight

        return -1

    def Dijkstra(self, source, target):
        visited = [False]*self.V #O(V)

        dist = [float('inf')]*self.V #O(V)
        dist[source] = 0

        h = [ (0, source) ] # (cost, node)
        while h: #O(E)
            cost, workingNode = heappop(h) #O(logV)
            if visited[workingNode]:
                continue

            if workingNode==target:
                return dist[workingNode]

            visited[workingNode] = True
            for index,neigh in enumerate(self.adj[workingNode]): # O(E)
                edgeWeight = self.weight[workingNode][index]
                if dist[workingNode]+edgeWeight < dist[neigh]:
                    dist[neigh] = dist[workingNode]+edgeWeight
                    heappush(h, (dist[neigh], neigh) ) #O(logE) = O(logV^2) = O(2logV)
        return dist

    def Kruskal_1(self):
        edges = [] # conjunto de arestas
        for node in range(self.V): # para cada nó no grafo
            for i in range(len(self.adj[node])): # para cada vizinho
                neigh = self.adj[node][i]
                weight = self.weight[node][i]
                # 1. criando a lista de arestas com peso
                edges.append( (weight, node, neigh) )

        # 2. Ordenar as arestas por peso
        edges.sort()

        # 3. criando o conjunto de subsets
        subsets = [i for i in range(self.V)]

        sum_of_edges = 0
        count_edges = 0
        # 4. para cada aresta
        for weight, source, target in edges:
            # 4.1 se as arestas fazem parte de conjuntos distintos
            if subsets[source]!=subsets[target]:
                # acumular o peso desta aresta
                sum_of_edges += weight
                save_subset = subsets[source]
                # 4.1.1 agrupar as duas arestas no mesmo conjunto
                for i in range(self.V):
                    if subsets[i]==save_subset:
                        subsets[i] = subsets[target]
                # contabilizando as arestas
                count_edges += 1
                # critério de parada
                if count_edges==self.V-1:
                    break

        return sum_of_edges

    def Kruskal_NoDisjointSets(self): # O(ElogE + EV)
        edges = []
        for node in range(self.V): #O(E)
            for i in range(len(self.adj[node])):
                neigh = self.adj[node][i]
                weight = self.weight[node][i]
                edges.append( (weight, node, neigh) )

        edges.sort() # O(ElogE)

        subsets = [i for i in range(self.V)] # O(V)

        sum_of_edges = 0
        count_edges = 0
        for weight, source, target in edges: #O(E)
            if subsets[source]!=subsets[target]:
                sum_of_edges += weight
                save_subset = subsets[source]
                for i in range(self.V): #O(V)
                    if subsets[i]==save_subset:
                        subsets[i] = subsets[target]
                count_edges += 1
                if count_edges==self.V-1:
                    break

        return sum_of_edges


    def Kruskal(self): # O(ElogE + V + ElogV) = O(ElogV) ou O(ElogE)
        edges = []
        for node in range(self.V): #O(E)
            for i in range(len(self.adj[node])):
                neigh = self.adj[node][i]
                weight = self.weight[node][i]
                edges.append( (weight, node, neigh) )

        edges.sort() # O(ElogE)

        subsets = DisjointSets(self.V)

        sum_of_edges = 0
        count_edges = 0
        for weight, source, target in edges: #O(E)
            if subsets.find(source)!=subsets.find(target):
                sum_of_edges += weight
                subsets.union(source, target) #O(logV)
                count_edges += 1
                if count_edges==self.V-1:
                    break

        return sum_of_edges

    def Prim(self): # O(ElogV)
        dist = [ float('inf') ] * self.V #O(V)
        dist[0] = 0

        visited = [False]*self.V # O(V)

        h = [ (0, 0) ]

        sum_of_edges = 0
        while h: #O(VlogE) = O(VlogV)
            cost, node = heappop(h)
            if visited[node]: continue
            visited[node] = True #O(V)
            sum_of_edges += cost

            for i in range(len(self.adj[node])): #O(E)
                neigh = self.adj[node][i]
                weight = self.weight[node][i]
                if not visited[neigh] and weight<dist[neigh]:
                    dist[neigh] = weight
                    heappush(h, (dist[neigh], neigh) )

        return sum_of_edges


    def Prim(self):
        # 1. Inicializar o peso (dist) de todos os nós para inf.
        dist = [ float('inf') ] * self.V
        # 2. 1o nó com peso zero
        dist[0] = 0
        # 3. Inicializar lista de visitados com false
        visited = [False]*self.V # O(V)
        # 4. Inicializar uma heap com 1o nó
        h = [ (0, 0) ]

        sum_of_edges = 0
        # 5. Enquanto houver nós na heap
        while h:
            # 5.1 Retirar o nó e peso da heap
            cost, node = heappop(h)
            # 5.2 Se o nó estiver sido visitado, continue
            if visited[node]: continue
            # 5.3 Marcar o nó como visitado
            visited[node] = True
            # 5.4 Acumular o custo ao acrescentar o nó v
            sum_of_edges += cost
            # 5.5 Para cada um dos vizinhos do nó v
            for i in range(len(self.adj[node])):
                neigh = self.adj[node][i]
                weight = self.weight[node][i]
                # 5.5.1 Se o vizinho não estiver sido visitado E
                # o peso for menor que o peso até o momento
                if not visited[neigh] and weight<dist[neigh]:
                    # 5.5.1.1 Atualizar o peso (dist) do vizinho
                    dist[neigh] = weight
                    # 5.5.1.2 Adiciona o vizinho na heap com o novo peso
                    heappush(h, (dist[neigh], neigh) )

        return sum_of_edges



g = Graph(6) # ignoring the 0 node
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(1, 4)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(2, 4)
g.addEdge(4, 2)
g.addEdge(2, 5)
g.addEdge(5, 2)
g.addEdge(3, 5)
g.addEdge(5, 3)
g.addEdge(4, 5)
g.addEdge(5, 4)
print( g.bfsList(1) )


g2 = Graph(8)
g2.addEdge(0, 1, 2)
g2.addEdge(1, 0, 2)
g2.addEdge(0, 2, 5)
g2.addEdge(2, 0, 5)
g2.addEdge(0, 3, 4)
g2.addEdge(3, 0, 4)
g2.addEdge(1, 2, 2)
g2.addEdge(2, 1, 2)
g2.addEdge(1, 4, 7)
g2.addEdge(4, 1, 7)
g2.addEdge(1, 6, 12)
g2.addEdge(6, 1, 12)
g2.addEdge(2, 3, 1)
g2.addEdge(3, 2, 1)
g2.addEdge(2, 4, 4)
g2.addEdge(4, 2, 4)
g2.addEdge(2, 5, 3)
g2.addEdge(5, 2, 3)
g2.addEdge(3, 5, 4)
g2.addEdge(5, 3, 4)
g2.addEdge(4, 5, 4)
g2.addEdge(5, 4, 4)
g2.addEdge(4, 7, 5)
g2.addEdge(7, 4, 5)
g2.addEdge(5, 7, 7)
g2.addEdge(7, 5, 7)
g2.addEdge(6, 7, 3)
g2.addEdge(7, 6, 3)

'''
print( g2.adj )
for u in range(8):
    print(u)
    print(g2.adj[u])
    print(g2.weight[u])
    print()
'''

print( 'From', 0, 'to', 7, g2.DijkstraWithoutHeap(0,7) )
print( 'From', 0, 'to', 7, g2.Dijkstra(0, 7) )


'''
Grafo com 7 nós

 5 A D
 5 C E
 6 D F
 7 A B
 7 B E
 8 B C
 8 E F
 9 B D
 9 E G
11 F G
15 D E
'''

g3 = Graph(7)
g3.addEdge(0, 3, 5) #5 A D
g3.addEdge(3, 0, 5) #5 A D
g3.addEdge(2, 4, 5) #5 C E
g3.addEdge(4, 2, 5) #5 C E
g3.addEdge(3, 5, 6) #6 D F
g3.addEdge(5, 3, 6) #6 D F
g3.addEdge(0, 1, 7) #7 A B
g3.addEdge(1, 0, 7) #7 A B
g3.addEdge(1, 4, 7) #7 B E
g3.addEdge(4, 1, 7) #7 B E
g3.addEdge(1, 2, 8) #8 B C
g3.addEdge(2, 1, 8) #8 B C
g3.addEdge(4, 5, 8) #8 E F
g3.addEdge(5, 4, 8) #8 E F
g3.addEdge(1, 3, 9) #9 B D
g3.addEdge(3, 1, 9) #9 B D
g3.addEdge(4, 6, 9) #9 E G
g3.addEdge(6, 4, 9) #9 E G
g3.addEdge(5, 6, 11) #11 F G
g3.addEdge(6, 5, 11) #11 F G
g3.addEdge(3, 4, 15) #15 D E
g3.addEdge(4, 3, 15) #15 D E

print('Kruskal no Disjoint Sets', g3.Kruskal_NoDisjointSets() )
print('Kruskal', g3.Kruskal() )
print('Prim', g3.Prim())