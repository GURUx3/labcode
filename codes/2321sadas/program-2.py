
graph = {
    'A': [['B'], ['C'], ['D']],
    'B': [['E', 'F']],
    'C': [['G'], ['H']],
    'D': [['I'], ['J']],
    'E': [], 'F': [], 'G': [], 'H': [],
    'I': [],
    'J': [['K', 'L']],
    'K': [], 'L': []
}

heuristic = {
    'A': 12, 'B': 10, 'C': 35, 'D': 36,
    'E': 17, 'F': 17, 'G': 18, 'H': 20,
    'I': 6, 'J': 9, 'K': 8, 'L': 7
}

solution_graph = {}

def compute_cost(children):
    cost = 0
    for child in children:
        cost += 1 + heuristic[child]
    return cost


def ao_star(node):
    if not graph[node]:
        return heuristic[node]

    min_cost = float('inf')
    best_children = None

    for option in graph[node]:
        cost = compute_cost(option)

        if cost < min_cost:
            min_cost = cost
            best_children = option

    heuristic[node] = min_cost
    solution_graph[node] = best_children

    for child in best_children:
        ao_star(child)

    return heuristic[node]


def print_final_path(node):
    path = [node]

    while node in solution_graph:
        children = solution_graph[node]
        path.extend(children)
        node = children[0]

    print("Final solution path:")
    print(" -> ".join(path))


ao_star('A')
print_final_path('A')
