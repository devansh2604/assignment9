#include <iostream>
using namespace std;
void dfsUtil(int **adj, int n, int u, bool *visited) {
    visited[u] = true;
    cout << u << ' ';
    for (int v=0; v<n; ++v) {
        if (adj[u][v] && !visited[v]) dfsUtil(adj, n, v, visited);
    }
}
void dfs(int **adj, int n, int start) {
    bool *visited = new bool[n];
    for (int i=0;i<n;++i) visited[i] = false;
    cout << "DFS order: ";
    dfsUtil(adj, n, start, visited);
    cout << '\n';
    delete[] visited;
}
int main() {
    int n;
    cout << "Enter number of vertices: ";
    if (!(cin >> n) || n <= 0) return 0;
    int **adj = new int*[n];
    for (int i=0;i<n;++i) {
        adj[i] = new int[n];
        for (int j=0;j<n;++j) adj[i][j] = 0;
    }
    cout << "Enter adjacency matrix (n x n) with 0/1 (row by row):\n";
    for (int i=0;i<n;++i)
        for (int j=0;j<n;++j)
            cin >> adj[i][j];
    int start;
    cout << "Enter start vertex (0-based): ";
    cin >> start;
    if (start < 0 || start >= n) start = 0;
    dfs(adj, n, start);
    for (int i=0;i<n;++i) delete[] adj[i];
    delete[] adj;
    return 0;
}
