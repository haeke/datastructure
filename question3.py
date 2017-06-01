"""
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
"""

"""
    Minimum spamming tree- make a graph with the smallest possible weight, using Kruskal's Algorithm

    kruskals algorithm is a greedy algorithm where we need to sort all the edges in non-decreasing order. after we pick the smallest edge we need to make sure that it does not form a cycle with the spanning tree formed so far, if it is not a cycle add the edge, if it is then skip over it. This process will continue until n - 1 where n is the number of edges

"""

s1 = {'A': [('B', 2)], 'B': [('A', 4), ('C', 2)], 'C': [('A', 2), ('B', 5)]}

#find the set of a an element
def findset(parent, i):
    if parent[i] == i:
        return i
    return findset(parent, parent[i])

#create a union of two sets by rank
def union(parent, rank, x, y):
    root_x = findset(parent, x)
    root_y = findset(parent, y)

    #check to see that the smaller rank tree is under a higher rank tree
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    #if the ranks are the same increment the rank by 1 and make it the root
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def MST(graph, verticies, inv_dict):
    #store the MST list that we want to return
    result = []

    #index for sorted edges
    sorted_edges = 0
    #index fdor the result list
    res_edges = 0

    #sort the edges in non-decreasing order of the weight
    graph = sorted(graph, key= lambda item: item[2])

    parent = []
    rank = []

    #create subset of the verticies with single elements
    for node in range(verticies):
        parent.append(node)
        rank.append(0)
    n = verticies - 1
    #loop through the number of edges minus 1
    if(res_edges < n):
        #pick the smallest edge and increment the index by one
        union_, vertex, weight = graph[sorted_edges]
        sorted_edges = sorted_edges + 1
        x = findset(parent, union_)
        y = findset(parent, vertex)

        #if the edges aren't a cycle, add it to the result
        if x != y:
            res_edges += 1
            result.append([union_, vertex, weight])
            union(parent, rank, x, y)

        #print the contents of the result list
        p1 = []
        final_result = {}
        for union_, vertex, weight in result:
            p1 = [(inv_dict[vertex],weight)]
            if (inv_dict[union_] not in final_result):
                final_result[inv_dict[union_]] = p1
            else:
                final_result[inv_dict[union_]] = final_result[inv_dict[union_]].append(p1)

        return final_result

def question3(s1):
    n = len(s1)
    tmp_dict = {}
    inv_dict = {}
    count = 0
    union_,verticies,weight = None, None, None
    graph = []
    for i in s1:
        tmp_dict[i] = count
        inv_dict[count] = i
        count += 1

    for i in s1:
        for j in s1[i]:
            union_,verticies,weight = tmp_dict[i], tmp_dict[j[0]], j[1]
            graph.append([union_,verticies,weight])
    print graph

    return MST(graph, count, inv_dict)


print question3(s1)
