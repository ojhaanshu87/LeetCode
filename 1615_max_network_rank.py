'''
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between
cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. 
If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.

Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
'''

# O(NlogN+N^2) at worst,  Sort by degree Method
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        # Build an adjacent list
        edges = defaultdict(list)
        for u, v in roads:
            edges[u].append(v)
            edges[v].append(u)
        # Calculate the degree for each vertex
        degree = []
        for i in range(n):
            degree.append((len(edges[i]), i))
        degree.sort(reverse=True)
        res = 0
        # Since the there are one edges coutned doubly at most, 
        # only need to consider the largest degrees and the second largest ones.
        for i in range(len(degree)):
            if degree[i][0] < degree[0][0]:
                break
            for j in range(i+1, len(degree)):
                if degree[j][0] < degree[1][0]:
                    break
                res = max(res, degree[i][0] + degree[j][0] - (degree[j][1] in edges[degree[i][1]]))
        return res
        
