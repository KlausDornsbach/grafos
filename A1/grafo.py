from collections import deque
# pylint: disable=no-member

class Node: 
    def __init__(self, id, label):
        self.label = label
        self.edges = {}
        self.degree = 0
        self.id = id

class NodeList:
    def __init__(self):
        self.n_vertices = 0
        self.n_edges = 0
        self.adjacency_list = []

    def getAdjacencyList(self):
        return self.adjacency_list

    def addNode(self, node):
        self.adjacency_list.append(node)
        self.n_vertices = self.n_vertices + 1

    def addEdge(self, a, b, weight):
        self.n_edges += 1
        self.adjacency_list[a-1].degree += 1
        self.adjacency_list[b-1].degree += 1
        self.adjacency_list[a-1].edges[b] = weight
        self.adjacency_list[b-1].edges[a] = weight

    def qtdVertices(self):
        return self.n_vertices

    def qtdArestas(self):
        return self.n_edges
    
    def grau(self, v):
        return self.adjacency_list[v-1].degree
    
    def rotulo(self, v):
        return self.adjacency_list[v-1].label
    
    def vizinhos(self, v):
        return self.adjacency_list[v-1].edges

    def haAresta(self, u, v):
        # print(self.adjacency_list[u-1].edges)
        return (v in self.adjacency_list[u-1].edges)

    def peso(self, u, v):
        if self.haAresta(u, v):
            return self.adjacency_list[u-1].edges[v]
        else:
            return float('inf')

    def ler(self, arquivo):
        edges = False
        with open(arquivo, 'r') as file:
            next(file)
            for line in file:
                if not edges:
                    if not line[0] == '*':  # adds nodes
                        var = line.split()
                        node = Node(int(var[0]), var[1])
                        self.addNode(node)
                    else:
                        edges = True
                else:                       # adds edges
                    var = line.split()
                    self.addEdge(int(var[0]), int(var[1]), float(var[2]))

    def transpose(self):
        for v in self.adjacency_list:
            for key in v.edges:
                self.addEdge(key, v.id, v.edges[key])
                del v.edges[key]

def hierholzer(grafo):
    adj_list = grafo.getAdjacencyList()
    for v in adj_list:  # populate edges list
        for k in v.edges:
            v.edges[k] = False  # exchange weight for bool value
    # that represents if I already crossed that edge 
    # don't forget to cross both (a->b) and (b->a)
    
    v = adj_list[0] # i'd rather use vertices, not id
    [r, cicle] = buscarSubcicloEuleriano(grafo, v)
    
    if r == False:
        return [False, None]
    else:
        for v in adj_list:  # populate edges list
            for k in v.edges:
                if v.edges[k] == False:
                    return [False, None]
        printHierholzer(1, cicle)
        return [True, cicle]
    

def buscarSubcicloEuleriano(grafo, v):
    adj_list = grafo.getAdjacencyList()
    cicle = []
    cicle.append(v)
    t = v

    while(1):
        # se não existe um nodo u vizinho de v e 
        # que aresta u->v não tenha sido visitada
        # retorno falso
        exists = False
        for key in v.edges:
            if v.edges[key] == False:
                exists = True
                pos = key
                break
        if not exists:
            return [False, None]
        else:
            adj_list[pos - 1].edges[v.id] = True
            v.edges[pos] = True
            v = adj_list[int(pos - 1)]
            cicle.append(v)
        if v == t:                 # test if ends while
            break
    # if exists some vertice 'u' in the cicle and any
    # of it's edges haven't been visited we call 
    # recursion

    for i in range(len(cicle)):
        v = cicle[i]
        for key in v.edges:
            if v.edges[key] == False: # didn't visit
                [r, inner_cicle] = buscarSubcicloEuleriano(grafo, v)
                if r == False:
                    return [False, None]
                cicle.pop(i)
                count = 0
                for j in range(i, len(inner_cicle)+i):
                    cicle.insert(j, inner_cicle[count])
                    count+=1
                
    return [True, cicle]

def printHierholzer(n, cicle):
    print(n)
    print(cicle[0].id, end='')
    for e in cicle[1:]:
        print(','+str(e.id), end='')
    print()


def buscaEmLargura(grafo, s):
    adj_list = grafo.getAdjacencyList()
    # print(adj_list)
    v = adj_list[s-1]

    distance = [float('inf')]*len(adj_list)
    ancestor = [None]*len(adj_list)
    visited_node = [False]*len(adj_list)

    distance[s-1] = 0
    visited_node[s-1] = True

    queue = deque([])
    queue.append(v)

    while len(queue) != 0:
        # print(queue[0].edges)
        u = queue.popleft()
        for key in u.edges: # dictionary entries
            # print(key)
            if visited_node[int(key) - 1] == False:
                visited_node[int(key) - 1] = True
                distance[int(key) - 1] = distance[u.id-1] + 1
                ancestor[int(key) - 1] = u.id
                queue.append(adj_list[int(key) - 1])

    return [distance, ancestor]

def printBuscaEmLargura(res):
    out = [None] * len(adj_list)

    for i in range(len(adj_list)): # print by distance
        out[i] = [res[0][i], i+1]

    ready_to_stringify = sorted(out, key=lambda l: l[0])

    # print(ready_to_stringify)
    count = 0
    print_count = True
    for i in range(len(ready_to_stringify)):
        var = ready_to_stringify[i][0]
        if count != var:  # ended line
            count+= 1
            print()
            print_count = True

        if print_count == True:
            print(str(var)+': '+str(ready_to_stringify[i][1]), end='')
            print_count = False
        else:
            print(','+str(ready_to_stringify[i][1]), end='')
    print()

def printBellmanFord(distance, ancestor, s):
    # print(s)
    for i in range(len(distance)):
        print(str(i+1)+": ", end='')
        path = []
        path.append(i+1)

        k = ancestor[i] - 1
        # print()
        while(k!=s-1):
            path.append(k+1)
            k = ancestor[k] - 1
        if i != s-1:
            path.append(s)
        path.reverse()
        print(str(path[0]), end='')
        for j in path[1:]:
            print(','+str(j), end='')
        print('; d='+str(distance[i]))

def bellmanFord(grafo, s):
    size = grafo.n_vertices
    # init
    distance = [float('inf')] * size
    ancestor = [None] * size
    distance[s-1] = 0
    ancestor[s-1] = s

    # iterations
    for i in range(1, size - 1):
        for v in grafo.getAdjacencyList():
            for e_key in v.edges:
                # relaxation
                # print('distance v: '+str(distance[int(e_key)-1])+', ')
                if distance[int(e_key)-1] > distance[v.id-1] + v.edges[e_key]:
                    distance[int(e_key)-1] = distance[v.id-1] + v.edges[e_key]
                    ancestor[int(e_key)-1] = v.id
    
    # check for negative cicles
    for v in grafo.getAdjacencyList():
        for e_key in v.edges:
            if  distance[int(e_key)-1] > distance[v.id-1] + v.edges[e_key]:
                return (False, null, null)
    printBellmanFord(distance, ancestor, s)
    return (True, distance, ancestor)


def printFloydWarshall(distance):
    for i in range(len(distance)):
        print(str(i+1)+':'+str(distance[i][0]), end='')
        for j in range(1, len(distance)):
            print(','+str(distance[i][j]), end='')
        print()
    print()

def floydWarshall(grafo):
    size = grafo.n_vertices
    adj_list = grafo.getAdjacencyList()
    distance = [[float('inf') for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if j == i:
                distance[i][j] = 0
                continue
            try:
                weight = adj_list[i].edges[j+1]
                distance[i][j] = weight
            except KeyError:
                continue

    for k in range(size):
        for u in range(size):
            for v in range(size):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
    printFloydWarshall(distance)


# adaptações para trabalho 2
# grafo dirigido

class DirectedNodeList(NodeList):
    def __init__(self):
        super().__init__(self)
    
    def addEdge(self, a, b, weight):
        self.n_edges += 1
        self.adjacency_list[a-1].degree += 1
        self.adjacency_list[a-1].edges[b] = weight


if __name__ == "__main__":
    
    n1 = Node(1, "john")
    n2 = Node(2, "bob")
    n3 = Node(3, "alice")

    node_list = NodeList()
    node_list.addNode(n1)
    node_list.addNode(n2)
    node_list.addNode(n3)

    node_list.addEdge(1, 2, 1.8)
    node_list.addEdge(2, 1, 1.8)
    node_list.addEdge(2, 3, 2.5)
    node_list.addEdge(3, 2, 2.5)

    # print(node_list.qtdArestas())
    # print(node_list.grau(1))
    # print(node_list.grau(2))
    # print(node_list.rotulo(1))
    # print(node_list.vizinhos(2))

    # print(node_list.haAresta(1, 2))
    # print(node_list.haAresta(3, 1))
    # print(node_list.peso(1, 2))
    # print(node_list.peso(3, 1))

    # node_list2 = NodeList()
    # adj_list = node_list2.getAdjacencyList()
    # node_list2.ler('agm_tiny.net')
   # node_list3 = NodeList()
   # node_list3.ler('entrada')
   # node_list4 = NodeList()
   # node_list4.ler('bellman')
    # for i in node_list3.getAdjacencyList():
    #     print(str(i.id)+": ", end='')
    #     print(i.edges)

    # for i in node_list3.getAdjacencyList():
    #     print(i.id)
    #     print(i.edges)

    # print(node_list2.getAdjacencyList()[0].label)
    # print(node_list2.getAdjacencyList()[1].label)
    # print(node_list2.haAresta(1,2))
    # print(node_list2.peso(1,2))
    # print(node_list2.haAresta(1,3))
    # print(node_list2.peso(1,3))
    # print(node_list2.haAresta(1,5))


    #res = buscaEmLargura(node_list2, 1)

    #printBuscaEmLargura(res)

    # res2 = hierholzer(node_list2)
    # print(res2)

    # res3 = hierholzer(node_list3)
    # res4 = bellmanFord(node_list4, 1)
    # print(res4[0])
    # print(res4[1])
    # print(res4[2])
    #floydWarshall(node_list4)



