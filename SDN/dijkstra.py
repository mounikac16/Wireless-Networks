from collections import defaultdict 

final = []

def minDistance(dist,queue): 
        # Initialize min value and min_index as -1 
    minimum = float("Inf") 
    min_index = -1
          
    for i in range(len(dist)): 
        if dist[i] < minimum and i in queue: 
            minimum = dist[i] 
            min_index = i 
    return min_index 
  
def printPath(parent, j,temp): 
      
    #Base Case : If j is source 
    if parent[j] == -1 : 
        temp.append(j) 
        print(j) 
        return
    printPath(parent , parent[j],temp)
    temp.append(j) 
    print(j) 
          
def printSolution(dist, parent): 
    src = 0
    for i in range(1, len(dist)): 
        temp = [] 
        printPath(parent,i,temp)
        final.append(temp) 
def dijkstra(graph, src): 

    row = len(graph) 
    col = len(graph[0]) 
    dist = [float("Inf")] * row 
  
    #Parent array to store  
    # shortest path tree 
    parent = [-1] * row 
  
    # Distance of source vertex  
    # from itself is always 0 
    dist[src] = 0
      
    # Add all vertices in queue 
    queue = [] 
    for i in range(row): 
        queue.append(i) 
              
    #Find shortest path for all vertices 
    while queue: 
        u = minDistance(dist,queue)  
  
        # remove min element      
        queue.remove(u) 

        for i in range(col): 
            if graph[u][i] and i in queue: 
                if dist[u] + graph[u][i] < dist[i]: 
                    dist[i] = dist[u] + graph[u][i] 
                    parent[i] = u 
  
  
    # print the constructed distance array 
    printSolution(dist,parent) 
   
# Print the solution 
dijkstra(graph,0) 
