#include <unordered_map>
#include <string.h>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

struct Node{
    string label;                       
    unordered_map<int,double> node_map; // edges
    int degree;                         // unordered_map size
    Node(string l) {                    // constructor
        label = l;                      
    }
};

template<typename T>
struct NodeList{
    int n_vertices;
    int n_edges;
    vector<T> adjacency_list;

    vector<T> getAdjacencyList() {
        return adjacency_list;
    }
    
    void addNode(T n) {
        adjacency_list.push_back(n);
        n_vertices++;
    }

    void addEdge(int a, int b, int weight) {
        n_edges = n_edges + 1;
        adjacency_list[a].node_map.insert({b, weight});
    }

    int qtdVertices() {
        return n_vertices;
    }
    
    int qtdArestas() {
        return n_edges/2;
    }

    int grau(int v) {
        return adjacency_list[v].degree;
    }

    string rotulo(int v) {  // retorna rotulo de v
        return adjacency_list[v].label;
    }

    unordered_map<int, double> vizinhos(int v) {
        return adjacency_list[v].node_map;
    }


};

int main() {
    // unordered_map<int,double> mymap = {{1, 1.0}, {2, 3.5}};
    // cout << mymap[2] << "\n";
    
    Node *n1 = new Node("marquinho dj");
    Node *n2 = new Node("sarah");
    Node *n3 = new Node("sadboy");
    NodeList<Node> nodelist;

    nodelist.addNode(n1);
    nodelist.addNode(n2);
    nodelist.addNode(n3);

    nodelist.getAdjacencyList();
    nodelist.qtdVertices();

    nodelist.addEdge(1, 2, 30);
    nodelist.addEdge(2, 1, 30);
    nodelist.addEdge(2, 3, 10);
    nodelist.qtdArestas();




    
    
    return 0;
}