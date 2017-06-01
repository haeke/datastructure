"""
    find a Minimum spanning tree by using Kruskal's algorithm
    given a connected, undirected, weighted tree

    this algorithm constructs an MST from given
"""
#
#
# from collections import defaultdict
#
# #Class to represent a graph
# class Graph:
#
#     def __init__(self,vertices):
#         self.V= vertices #No. of vertices
#         self.graph = [] # default dictionary to store graph
#
#
#     # function to add an edge to graph
#     def addEdge(self,u,v,w):
#         self.graph.append([u,v,w])
#
#     # A utility function to find set of an element i
#     # (uses path compression technique)
#     def find(self, parent, i):
#         if parent[i] == i:
#             return i
#         return self.find(parent, parent[i])
#
#     # A function that does union of two sets of x and y
#     # (uses union by rank)
#     def union(self, parent, rank, x, y):
#         xroot = self.find(parent, x)
#         yroot = self.find(parent, y)
#
#         # Attach smaller rank tree under root of high rank tree
#         # (Union by Rank)
#         if rank[xroot] < rank[yroot]:
#             parent[xroot] = yroot
#         elif rank[xroot] > rank[yroot]:
#             parent[yroot] = xroot
#         #If ranks are same, then make one as root and increment
#         # its rank by one
#         else :
#             parent[yroot] = xroot
#             rank[xroot] += 1
#
#     # The main function to construct MST using Kruskal's algorithm
#     def KruskalMST(self):
#
#         result =[] #This will store the resultant MST
#
#         i = 0 # An index variable, used for sorted edges
#         e = 0 # An index variable, used for result[]
#
#         #Step 1:  Sort all the edges in non-decreasing order of their
#         # weight.  If we are not allowed to change the given graph, we
#         # can create a copy of graph
#         self.graph =  sorted(self.graph,key=lambda item: item[2])
#         #print self.graph
#
#         parent = [] ; rank = []
#
#         # Create V subsets with single elements
#         for node in range(self.V):
#             parent.append(node)
#             rank.append(0)
#
#         # Number of edges to be taken is equal to V-1
#         while e < self.V -1 :
#
#             # Step 2: Pick the smallest edge and increment the index
#             # for next iteration
#             u,v,w =  self.graph[i]
#             i = i + 1
#             x = self.find(parent, u)
#             y = self.find(parent ,v)
#
#             # If including this edge does't cause cycle, include it
#             # in result and increment the index of result for next edge
#             if x != y:
#                 e = e + 1
#                 result.append([u,v,w])
#                 self.union(parent, rank, x, y)
#             # Else discard the edge
#
#         # print the contents of result[] to display the built MST
#         print "Following are the edges in the constructed MST"
#         for u,v,weight  in result:
#             print str(u) + " -- " + str(v) + " == " + str(weight)
#             #print ("%d -- %d == %d" % (u,v,weight))
#
#
# g = Graph(4)
# g.addEdge(0, 1, 10)
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)
#
# g.KruskalMST()


"""
Given an undirected graph G, find the minimum spanning tree within G. A minimum
spanning tree connects all vertices in a graph with the smallest possible total
weight of edges. Your function should take in and return an adjacency list
structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
"""
# A utility function to find set of an element i
# (uses path compression technique)
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# A function that does union of two sets of x and y
# (uses union by rank)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of high rank tree
    # (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    #If ranks are same, then make one as root and increment
    # its rank by one
    else :
        parent[yroot] = xroot
        rank[xroot] += 1

# The main function to construct MST using Kruskal's algorithm
def KruskalMST(graph, V, inv_dict):

    result =[] #This will store the resultant MST

    i = 0 # An index variable, used for sorted edges
    e = 0 # An index variable, used for result[]

    #Step 1:  Sort all the edges in non-decreasing order of their
    # weight.  If we are not allowed to change the given graph, we
    # can create a copy of graph
    graph =  sorted(graph,key=lambda item: item[2])
    #print self.graph

    parent = [] ; rank = []

    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < V -1 :

        # Step 2: Pick the smallest edge and increment the index
        # for next iteration
        u,v,w =  graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent ,v)

        # If including this edge does't cause cycle, include it
        # in result and increment the index of result for next edge
        if x != y:
            e = e + 1
            result.append([u,v,w])
            union(parent, rank, x, y)
        # Else discard the edge

    # print the contents of result[] to display the built MST
    #print "Following are the edges in the constructed MST"
    p1 = []
    final_result = {}
    for u,v,weight  in result:
        p1 = [(inv_dict[v],weight)]
        if inv_dict[u] not in final_result:
            final_result[inv_dict[u]] = p1
        else:
            final_result[inv_dict[u]] = final_result[inv_dict[u]].append(p1)
        #print str(u) + " -- " + str(v) + " == " + str(weight)
        #print ("%c -- %c == %d" % (inv_dict[u],inv_dict[v],weight))

    return final_result

def question3(s1):
    n = len(s1)
    tmp_dict = {}
    inv_dict = {}
    count = 0
    u,v,w = None, None, None
    graph = []
    for i in s1:
        tmp_dict[i] = count
        inv_dict[count] = i
        count += 1
    #print tmp_dict

    for i in s1:
        for j in s1[i]:
            #print tmp_dict[i], tmp_dict[j[0]], j[1]
            u,v,w = tmp_dict[i], tmp_dict[j[0]], j[1]
            graph.append([u,v,w])
    #print graph

    return KruskalMST(graph, count, inv_dict)


# Main program
def main():
    s1 = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}
    print question3(s1)

if __name__ == '__main__':
    main()
