#Initialize hash table for Dijkstra
#Hash table for graph incl. weight of each node
graph = {}
#Hash table within hash table
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["end"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5
graph["end"] = {}
#Hash table for cost from start node
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity
#Hash Table for parents of each node
parent = {}
parent["a"] = "start"
parent["b"] = "start"
parent["end"] = None
#List to track all processed nodes
processed = []

#Improvement: print shortest path
def dijkstra(graph, costs, parent):
    node = find_lowest_cost_node(costs)
    #Loop until no possible lowest node to check
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        #Loop through neighbors of lowest cost node
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parent[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs, parent

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

#Lowest cost to each graph node from starting node
path_cost, path_parent = dijkstra(graph, costs, parent)
print(path_cost)
print(path_parent)