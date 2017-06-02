"""
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
"""

"""
    I used kruskals algorithm to create the minimum spanning tree. This algorithm requires that I sort all the edges in non-decreasing order of their weight. after we pick the smallest edge we need to make sure that it does not form a cycle with the spanning tree formed so far, if it is not a cycle add the edge with a union, if it is then skip over it. This process will continue until n - 1 where n is the number of verticies.

    the complexity is O(ElogE) where E are the number of edges

"""

#find a set that belongs to the parent
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

#create a union of two sets, x and y by rank if they are the same then make the root one
def union(parent, rank, x, y):
    rootx = find(parent, x)
    rooty = find(parent, y)

    if rank[rootx] < rank[rooty]:
        parent[rootx] = rooty
    elif rank[rootx] > rank[rooty]:
        parent[rooty] = rootx
    #handle same ranks
    else:
        parent[rooty] = rootx
        rank[rootx] += 1

def MST(graph, vertex, inv_dict):
    result = []

    i = 0
    e = 0

    #sort the graph provided in non-decreasing order
    graph = sorted(graph, key=lambda item: item[2])

    parent = []
    rank = []

    #create V subsets with single Nodes
    for node in range(vertex):
        parent.append(node)
        rank.append(0)

    n = vertex - 1

    while e < n:
        #pick the smallest edge and increment the index
        u,v,w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        #make sure edges aren't the same or a cycle will occur
        #add it to the result list and increment the index for the next edge
        if x != y:
            e += 1
            result.append([u,v,w])
            union(parent, rank, x, y)

    #print what is in result list - aka the MST
    p1 = []
    final_result = {}
    for u,v,weight in result:
        p1 = [(inv_dict[v], weight)]
        if inv_dict[u] not in final_result:
            final_result[inv_dict[u]] = p1
        else:
            final_result[inv_dict[u]] = final_result[inv_dict[u]].append(p1)

    return final_result

def question3(s1):

    tmp_dict = {}
    inv_dict = {}
    count = 0
    #store the nodeto, nodefrom and weight
    u,v,w = None, None, None
    graph = []

    for i in s1:
        tmp_dict[i] = count
        inv_dict[count] = i
        count += 1
   #iterate through the
    for i in s1:
        for j in s1[i]:
            u,v,w = tmp_dict[i], tmp_dict[j[0]], j[1]
            graph.append([u,v,w])

    return MST(graph, count, inv_dict)

s1 = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}

print question3(s1)
