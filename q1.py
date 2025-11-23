# Graph algorithms: BFS, DFS, Kruskal, Prim, Dijkstra
from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight=1.0):
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def bfs(self, start):
        from collections import deque
        visited, order, parent = set(), [], {start: None}
        q = deque([start]); visited.add(start)
        while q:
            u = q.popleft(); order.append(u)
            for v, _ in self.adj[u]:
                if v not in visited:
                    visited.add(v); parent[v]=u; q.append(v)
        return order, parent

    def dfs(self, start):
        visited, order, parent = set(), [], {start: None}
        stack=[start]
        while stack:
            u = stack.pop()
            if u in visited: continue
            visited.add(u); order.append(u)
            for v, _ in reversed(self.adj[u]):
                if v not in visited:
                    parent[v]=u; stack.append(v)
        return order, parent

    def kruskal_mst(self):
        if self.directed: raise ValueError("Kruskal requires undirected graph")
        edges=[]; seen=set()
        for u in self.adj:
            for v,w in self.adj[u]:
                key=tuple(sorted((u,v)))
                if key not in seen: seen.add(key); edges.append((w,u,v))
        edges.sort()
        parent={}; rank={}
        def find(x):
            parent.setdefault(x,x)
            if parent[x]!=x: parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rx,ry=find(x),find(y)
            if rx==ry: return False
            if rank.get(rx,0)<rank.get(ry,0): parent[rx]=ry
            else:
                parent[ry]=rx
                if rank.get(rx,0)==rank.get(ry,0): rank[rx]=rank.get(rx,0)+1
            return True
        mst=[]; total=0
        for w,u,v in edges:
            if union(u,v):
                mst.append((u,v,w)); total+=w
        return mst, total

    def prim_mst(self, start=None):
        if self.directed: raise ValueError("Prim requires undirected graph")
        nodes=list(self.adj.keys())
        if not nodes: return [],0
        if start is None: start=nodes[0]
        visited=set([start]); heap=[]
        for v,w in self.adj[start]: heapq.heappush(heap,(w,start,v))
        mst=[]; total=0
        while heap and len(visited)<len(self.adj):
            w,u,v=heapq.heappop(heap)
            if v in visited: continue
            visited.add(v); mst.append((u,v,w)); total+=w
            for nxt,wt in self.adj[v]:
                if nxt not in visited: heapq.heappush(heap,(wt,v,nxt))
        return mst, total

    def dijkstra(self, source):
        dist={source:0}; parent={source:None}; pq=[(0,source)]
        while pq:
            d,u=heapq.heappop(pq)
            if d>dist.get(u,float('inf')): continue
            for v,w in self.adj[u]:
                nd=d+w
                if nd<dist.get(v,float('inf')):
                    dist[v]=nd; parent[v]=u; heapq.heappush(pq,(nd,v))
        return dist, parent

if __name__=='__main__':
    g=Graph(directed=False)
    edges=[('A','B',4),('A','C',2),('B','C',1),('B','D',5),('C','D',8),('C','E',10),('D','E',2),('D','F',6),('E','F',3)]
    for u,v,w in edges: g.add_edge(u,v,w)
    print("BFS from A:", g.bfs('A')[0])
    print("DFS from A:", g.dfs('A')[0])
    print("Kruskal MST:", g.kruskal_mst())
    print("Prim MST:", g.prim_mst('A'))
    print("Dijkstra from A:", g.dijkstra('A'))
