#graph as a dictionary

graph = {
    "A" : {"B", "C"},
    "B":{"A","D"},
    "C":{"A","E"},
    "D":{"B"},
    "E":{"C"}

}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    
            dfs(graph, "E")
    
        return visited
    