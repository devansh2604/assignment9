#include <iostream>
using namespace std;
class Queue {
    int *data;
    int capacity;
    int head, tail, sz;
public:
    Queue(int cap=1000): capacity(cap), head(0), tail(0), sz(0) {
        data = new int[capacity];
    }
    ~Queue(){ delete[] data; }
    bool empty() const { return sz == 0; }
    void push(int x) {
        if (sz == capacity) return;
        data[tail] = x;
        tail = (tail + 1) % capacity;
        ++sz;
    }
    int pop() {
        if (sz == 0) return -1;
        int v = data[head];
        head = (head + 1) % capacity;
        --sz;
        return v;
    }
};
void bfs(int **adj, int n, int start) {
    bool *visited = new bool[n];
    for (int i=0;i<n;++i) visited[i] = false;
    Queue q(n+5);
    visited[start] = true;
    q.push(start);
    cout << "BFS order: ";
    while (!q.empty()) {
        int u = q.pop();
        cout << u << ' ';
        for (int v=0; v<n; ++v) {
            if (adj[u][v] && !visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
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
    bfs(adj, n, start);
    for (int i=0;i<n;++i) delete[] adj[i];
    delete[] adj;
    return 0;
}
