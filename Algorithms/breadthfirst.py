from collections import deque
#Initalize graph to search through
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

#Breadth-first search of graph for shortest path between nodes
#(Improvement: return search path and # of edges)
def bfs(graph, startnode, endnode):
    #Track visited nodes
    visited = []
    search_queue = deque()
    search_queue += graph[startnode]
    #if startnode == endnode:
    #    return True
    #Start search from given node
    while search_queue:
        #Check node in front of queue
        check_node = search_queue.popleft()
        if check_node not in visited:
            if check_node == endnode:
                print("A path was found!")
                return
            else:
                #If desired node not found, add subnodes to search queue
                search_queue += graph[check_node]
                #Append currently checked node to visited list
                visited.append(check_node)
    print("No path was found")

bfs(graph, "bob", "jonny")