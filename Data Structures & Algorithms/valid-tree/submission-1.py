class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #main thing about trees is other children dont connect to parents, we pass previous because its undirected and we trying to detect loops
        if not n:
            return True #emptry graph tech is tree
        #create adjancecy list for all connections
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            #for each list we append n1 and n2 we addd all connections both way
            adj[n1].append(n2)# and reverse of this bc its 2 nodes connected
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):# need to check prev for no false pos and i is value we passing
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):# i is where we r coming from, and in our if this still runs
                    return False# detected loop
            return True# went thru all neighbors
        return dfs(0, -1) and n == len(visit) # prev is -1 bc it never exists and connectivity good bc no extra nodes visisted




        