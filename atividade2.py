import grafo 

def dfsVisit(G, v, C, T, A, F, tempo):
    neighbour_list_v = G.getAdjacencyList()[v-1]
    C[v-1] = True
    tempo = tempo + 1
    T[v-1] = tempo
    for key in neighbour_list_v:
        if neighbour_list_v[key] == False:
            A[key-1] = v
            dfsVisit(G, v, C, T, A, F, tempo)
    tempo = tempo + 1
    F[v-1] = [tempo, F[v-1][1]]

def dfs(G):
    # variable definition/initialization
    node_list = G.getAdjacencyList()
    size = len(node_list)
    C = [False] * size
    T = [float('inf')] * size
    A = [None] * size
    for i in F:     # for future sorting, know wich id is with wich time
        i.append(i)
    tempo = 0

    for u in node_list:
        if C[u.id - 1] == False:
            dfsVisit(G, u, C, T, A, F, tempo)

    return [C, T, A, F]

def stronglyConnectedComponents(G):
    [C, T, Al, F] = dfs(G)
    # create transposed graph
    Gt = G.transpose()
    # sort elements by F


if __name__ == "__main__":
    #n1 = grafo.Node(1, "john")
    lista = grafo.DirectedNodeList()
    lista.ler("entrada")
    #lista.addNode(n1)
    lista.printAll()
    listaTrans = lista.transpose()
    listaTrans.printAll()