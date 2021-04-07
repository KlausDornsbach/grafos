import grafo 

# QUESTAO 1 IMPLEMENTAÇÂO:
def dfsVisit(G, v, C, T, A, F, tempo):
    pos = v.id - 1
    neighbour_list_v = G.getAdjacencyList()[pos]
    C[pos] = True
    tempo = tempo + 1
    T[pos] = tempo

    for key in neighbour_list_v.edges:
        if C[key-1] == False:
            A[key-1] = v.id
            u = G.getAdjacencyList()[key-1]
            tempo = dfsVisit(G, u, C, T, A, F, tempo)

    tempo = tempo + 1
    F[pos] = [tempo, F[pos][1]]

    return tempo

def dfsVisit_mod(G, v, C, T, A, F, tempo, tabela_id_posicao):
    pos = tabela_id_posicao[v.id-1]
    neighbour_list_v = G.getAdjacencyList()[pos]
    C[pos] = True
    tempo = tempo + 1
    T[pos] = tempo
    
    for key in neighbour_list_v.edges:
        key_pos = tabela_id_posicao[key-1]
        if C[key_pos] == False:
            A[key_pos] = v.id
            u = G.getAdjacencyList()[key_pos]
            tempo = dfsVisit_mod(G, u, C, T, A, F, tempo, tabela_id_posicao)
    
    tempo = tempo + 1
    F[pos] = [tempo, F[pos][1]]
    
    return tempo
    
def dfs(G):
    # variable definition/initialization
    node_list = G.getAdjacencyList()
    size = len(node_list)
    C = [False] * size
    T = [float('inf')] * size
    F = []
    A = [None] * size
    
    for i in range(size):     # for future sorting, know wich id is with wich time
        F.append([])
        F[i].append(float('inf'))
        F[i].append(i)
    tempo = 0

    for u in node_list:
        if C[u.id - 1] == False:
            tempo = dfsVisit(G, u, C, T, A, F, tempo)

    return [C, T, A, F]

def dfs_mod(G, tabela_id_posicao):
    # variable definition/initialization
    node_list = G.getAdjacencyList()
    size = len(node_list)
    C = [False] * size
    T = [float('inf')] * size
    F = []
    A = [None] * size
    
    for i in range(size):     # for future sorting, know wich id is with wich time
        F.append([])
        F[i].append(float('inf'))
        F[i].append(i)  
    tempo = 0

    for u in node_list:
        if C[tabela_id_posicao[u.id - 1]] == False:
            tempo = dfsVisit_mod(G, u, C, T, A, F, tempo, tabela_id_posicao)

    return [C, T, A, F]

def stronglyConnectedComponents(G):
    [C, T, Al, F] = dfs(G)
    # create transposed graph
    Gt = G.transpose()
    # sort elements of F
    F.sort(reverse=True, key=lambda x:x[0])
    new_graph = grafo.DirectedNodeList()
    tabela_id_posicao = [None] * len(G.getAdjacencyList())
    cont = 0

    for i in F:
        tabela_id_posicao[i[1]] = cont
        new_graph.addNode(Gt.getAdjacencyList()[i[1]])
        cont += 1
    
    [V, B, Anc, M] = dfs_mod(new_graph, tabela_id_posicao)

    return [Anc, new_graph]

def printStronglyConnectedComponents(L, G):
    cont = 0
    while(cont < len(L)):
        output = []

        if(L[cont] == None):
            output.append(G.getAdjacencyList()[cont].id)
            cont += 1
            while(cont < len(L) and L[cont] != None):
                output.append(G.getAdjacencyList()[cont].id)
                cont += 1
        print(output[0], end='')

        for i in output[1:]:
            print(","+str(i), end='')
        print()




# QUESTAO 2 IMPLEMENTACAO:

def ordenacaoTopologica(G):

    # variable declaration/init
    size = len(G.getAdjacencyList())

    C = [False] * size
    T = [float('inf')] * size
    F = [float('inf')] * size
    tempo = 0

    # output list
    O = []

    for i in G.getAdjacencyList():
        if C[i.id - 1] == False:
            dfsVisitOT(G, i, C, T, F, tempo, O)

    return O

def dfsVisitOT(G, u, C, T, F, tempo, O):
    C[u.id - 1] = True
    tempo += 1
    T[u.id - 1] = tempo

    for key in u.edges:
        if C[key - 1] == False:
            dfsVisitOT(G, G.getAdjacencyList()[key - 1], C, T, F, tempo, O)

    tempo += 1
    F[u.id - 1] = tempo

    O.insert(0, u.label)



# QUESTAO 3

def kruskal(G):
    node_list = G.getAdjacencyList()
    A = set([])
    S = []
    for i in range(len(node_list)):
        S.append(set([]))
        S[i].add(node_list[i].id)
    
    # Edge list
    E = []
    for i in node_list:
        for k in i.edges:
            E.append((k, i.id, i.edges[k]))
    
    # sort by weight
    E.sort(reverse=False, key=lambda x:x[2])

    for e in E:
        if S[e[0]-1].isdisjoint(S[e[1]-1]):
            A.add(e)
            x = S[e[0]-1] | S[e[1]-1]
            for y in x:
                S[y-1] = x
    
    return A

def printKruskal(A):
    sum = 0
    for i in A: 
        sum += i[2]
    print(sum)  # print cost sum

    for e in A: # print first element
        print(str(e[0]) + "-" + str(e[1]), end='')
        A.remove(e)
        break
    for i in A: # print rest
        print(", " + str(i[0]) + "-" + str(i[1]), end='')
    print()


def prim(G):
    node_list = G.getAdjacencyList()
    # define root node
    r = node_list[0]
    # define vector of predecessor A and cost vector K
    A = [None] * len(node_list)
    K = [float('inf')] * len(node_list)

    K[r.id - 1] = 0

    # define priority structure
    # Q = 

# MAIN
    
if __name__ == "__main__":
    #n1 = grafo.Node(1, "john")
    lista = grafo.DirectedNodeList()
    lista.ler("entrada")    # mudar aqui arquivo para teste (inculir no mesmo
                            # diretorio que atividade2.py)
    #lista.addNode(n1)
    # lista.printAll()
    # listaTrans = lista.transpose()
    # print("--------------------")
    # listaTrans.printAll()

    # QUESTAO 1:
    # [anc, Gt] = stronglyConnectedComponents(lista)
    # printStronglyConnectedComponents(anc, Gt)


    # QUESTAO 2:
    # O = ordenacaoTopologica(lista)
    # print(O)


    # QUESTAO 3:
    A = kruskal(lista)
    printKruskal(A)

    # out = dfs(lista)
    # print(out[0])
    # print(out[1])
    # print(out[2])
    # print(out[3])

