"""
    adjacency list representation of a graph -
"""

"""
    implemented using a list of lists
"""
#
# adjacency_list = [ [1,2], [2,3], [3], [5,6], [] ]
#
# print("list of neighbors at vertex 0: ", adjacency_list[0])
# print("list of neighbors at vertex 3: ", adjacency_list[3])
#
# print("\n all adjacency lists with corresponding vertexes")
# n = len(adjacency_list)
# for vertex in range(0,n):
#     print(vertex, ": ", adjacency_list[vertex])

"""
    implemented using a dictionary of key, value pairs
"""

adjList_dict = {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5), ('A', 7), ('D', 8)]}

for i in adjList_dict:
    print i , adjList_dict[i]
