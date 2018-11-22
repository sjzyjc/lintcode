class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        
        in_degree = {}
        for node in graph:
            in_degree[node] = 0
        
        for node in graph:
            for neighbor in node.neighbors:
                in_degree[neighbor] += 1
        
        stack = []
        for node in in_degree:
            if in_degree[node] == 0:
                stack.append(node)

        ret = []
        while stack:
            node = stack.pop()
            ret.append(node)
            for neighbor in node.neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)
        
        return ret