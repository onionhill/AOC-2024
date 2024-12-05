from collections import deque


## https://www.youtube.com/watch?v=cIBFEhD77b4
def sort_nodes(edges: list[list[str]], updates: list[str]) :

    graph = {update: [] for update in updates}
    in_degree = {update: 0 for update in updates}
    ## 75,47,61,53,29
    ## Graph: {'75': [], '47': [], '61': [], '53': [], '29': []}
    ## in_degree: {'75': 0, '47': 0, '61': 0, '53': 0, '29': 0}

    for node_a, node_b in edges:
        if node_a in updates and node_b in updates:
            graph[node_a].append(node_b)
            in_degree[node_b] += 1

    ## Graph: {
    #   '75': ['29', '53', '47', '61'], 
    #   '47': ['53', '61', '29'], 
    #   '61': ['53', '29'], 
    #   '53': ['29'], '29': []}
    # 
    # in_degree {
    # '75': 0,  SAFE
    # '47': 1, 
    # '61': 2, 
    # '53': 3, 
    # '29': 4}
   

    # Henter alle noder som har tallet 0 in_degree
    start_nodes = [node for node, nodeID in in_degree.items() if nodeID == 0]
    sorted_nodes = []
    queue = deque(start_nodes)
    while queue:
        current = queue.pop() ## 75
        sorted_nodes.append(current)
        for node in graph[current]: # '75': ['29', '53', '47', '61'], 
            in_degree[node] -= 1
            # Etter updates ser nå in_degree slik ut 
            # {'75': 0, 
            # '47': 0,  ## NY SAFE
            # '61': 1, 
            # '53': 2, 
            # '29': 3}
            if in_degree[node] == 0:
                queue.append(node) ## 47 legges inn her


    if len(sorted_nodes) != len(updates):
        raise Exception("Something went wrong!")

    return sorted_nodes

def read_file(filename):
    with open(filename, 'r') as file:
        input_data = file.read()

    rules, updates = input_data.split("\n\n")
    edges = [rule.split("|") for rule in rules.splitlines()]

    
    return rules, updates, edges



rules, updates, edges = read_file('input.txt')


part1_sum = 0
part2_sum = 0

for line in updates.splitlines():
    updates = line.split(",")
    sorted_updates = sort_nodes(edges, updates)
    if updates == sorted_updates:
        part1_sum += int(updates[len(updates) // 2])
    else:
        part2_sum += int(sorted_updates[len(sorted_updates) // 2])
print("Part 1 " , part1_sum)
print("Part 2 " , part2_sum)
