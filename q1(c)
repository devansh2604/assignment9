#include <iostream>
#include <climits>
using namespace std;
struct Edge {
    int u, v;
    int w;
};
class UnionFind {
    int *parent, *rankv;
    int n;
public:
    UnionFind(int n_): n(n_) {
        parent = new int[n];
        rankv  = new int[n];
        for (int i=0;i<n;++i) { parent[i]=i; rankv[i]=0; }
    }
    ~UnionFind(){ delete[] parent; delete[] rankv; }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int a, int b) {
        int pa = find(a), pb = find(b);
        if (pa == pb) return false;
        if (rankv[pa] < rankv[pb]) parent[pa] = pb;
        else if (rankv[pb] < rankv[pa]) parent[pb] = pa;
        else { parent[pb] = pa; rankv[pa]++; }
        return true;
    }
};
void sortEdgesByWeight(Edge *edges, int m) {
    for (int i=0;i<m-1;++i) {
        int minIdx = i;
        for (int j=i+1;j<m;++j)
            if (edges[j].w < edges[minIdx].w) minIdx = j;
        if (minIdx != i) {
            Edge tmp = edges[i];
            edges[i] = edges[minIdx];
            edges[minIdx] = tmp;
        }
    }
}
void kruskalMST(Edge *edges, int m, int n) {
    sortEdgesByWeight(edges, m);
    UnionFind uf(n);
    int totalWeight = 0;
    cout << "Kruskal MST edges (u v w):\n";
    int taken = 0;
    for (int i=0;i<m && taken < n-1; ++i) {
        if (uf.unite(edges[i].u, edges[i].v)) {
            cout << edges[i].u << ' ' << edges[i].v << ' ' << edges[i].w << '\n';
            totalWeight += edges[i].w;
            ++taken;
        }
    }
    cout << "Total weight (Kruskal): " << totalWeight << '\n';
}
void primMST(int **wt, int n) {
    const int INF = INT_MAX / 4;
    int *key = new int[n];
    bool *inMST = new bool[n];
    int *parent = new int[n];

    for (int i=0;i<n;++i) { key[i]=INF; inMST[i]=false; parent[i]=-1; }
    key[0] = 0;

    for (int count=0; count<n-1; ++count) {
        int u = -1;
        int best = INF;
        for (int v=0; v<n; ++v) {
            if (!inMST[v] && key[v] < best) { best = key[v]; u = v; }
        }
        if (u == -1) break;
        inMST[u] = true;
        for (int v=0; v<n; ++v) {
            if (wt[u][v] >= 0 && !inMST[v] && wt[u][v] < key[v]) {
                key[v] = wt[u][v];
                parent[v] = u;
            }
        }
    }
    int total = 0;
    cout << "Prim MST edges (u v w):\n";
    for (int v=1; v<n; ++v) {
        if (parent[v] != -1) {
            cout << parent[v] << ' ' << v << ' ' << wt[parent[v]][v] << '\n';
            total += wt[parent[v]][v];
        }
    }
    cout << "Total weight (Prim): " << total << '\n';

    delete[] key; delete[] inMST; delete[] parent;
}
int main() {
    int n;
    cout << "Enter number of vertices (undirected graph): ";
    if (!(cin >> n) || n <= 0) return 0;
    int **wt = new int*[n];
    for (int i=0;i<n;++i) {
        wt[i] = new int[n];
        for (int j=0;j<n;++j) wt[i][j] = -1;
    }
    cout << "Enter adjacency weight matrix (n x n). Use -1 or 0 for no edge (if you prefer 0 as no edge, keep diagonal 0):\n";
    for (int i=0;i<n;++i)
        for (int j=0;j<n;++j)
            cin >> wt[i][j];
    int maxEdges = n*(n-1)/2;
    Edge *edges = new Edge[maxEdges];
    int m = 0;
    for (int i=0;i<n;++i) {
        for (int j=i+1;j<n;++j) {
            if (wt[i][j] >= 0) {
                edges[m].u = i;
                edges[m].v = j;
                edges[m].w = wt[i][j];
                ++m;
            }
        }
    }
    if (m == 0) {
        cout << "No edges present.\n";
    } else {
        kruskalMST(edges, m, n);
        primMST(wt, n);
    }
    delete[] edges;
    for (int i=0;i<n;++i) delete[] wt[i];
    delete[] wt;
    return 0;
}
