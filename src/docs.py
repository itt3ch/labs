from collections import defaultdict

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)


    graph_copy = graph.copy()

    for node in graph_copy:
        if node not in visited:
            dfs(node)

    return stack[::-1]
    
def main():
    graph = defaultdict(list)

    with open("govern.in", "r") as f:
        for line in f:
            dependency, node = line.strip().split()
            graph[node].append(dependency)

    sorted_order = topological_sort(graph)

    with open("govern.out", "w") as f:
        for node in sorted_order:
            f.write(node + "\n")

if __name__ == "__main__":
    main()
