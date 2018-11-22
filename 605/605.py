from collections import deque
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        
        in_degree = {}
        next_node ={}
        
        for seq in seqs:
            for index, num in enumerate(seq):
                if num not in in_degree:
                    in_degree[num] = 0
                if num not in next_node:
                    next_node[num] = []
                
                if index >= 1:
                    in_degree[num] += 1
                
                if index < len(seq) - 1:
                    next_node[num].append(seq[index + 1])
                    
        queue = deque()
        ret = []
        for key in in_degree:
            if in_degree[key] == 0:
                queue.append(key)
        
        while queue:
            size = len(queue)
            
            if size > 1:
                return False
            
            for i in range(size):
                node = queue.popleft()
                ret.append(node)
            
                for nextt in next_node[node]:
                    in_degree[nextt] -= 1
            
                    if in_degree[nextt] == 0:
                        queue.append(nextt)
                    
        return ret == org            