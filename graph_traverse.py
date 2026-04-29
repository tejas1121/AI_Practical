# -------- INPUT --------
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

# adjacency list using simple loop
graph = []
for i in range(V):
    graph.append([])

print("Enter edges (u v):")
for i in range(E):
    edge = input().split()   # take input as list of strings
    u = int(edge[0])
    v = int(edge[1])

    graph[u].append(v)
    graph[v].append(u)   # undirected


# -------- DFS --------
def dfs(node, visited):
    visited[node] = True
    print(node, end=" ")
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited)


# -------- BFS --------
def bfs(start):
    visited = []
    for i in range(V):
        visited.append(False)

    queue = []
    
    visited[start] = True
    queue.append(start)

    while len(queue) != 0:
        node = queue.pop(0)
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


# -------- RUN --------
print("\nDFS Traversal:")
visited = []
for i in range(V):
    visited.append(False)

dfs(0, visited)

print("\n\nBFS Traversal:")
bfs(0)