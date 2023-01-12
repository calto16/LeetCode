from collections import defaultdict,Counter
class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        
        edge = defaultdict(set)
        for a,b in edges:
            edge[a].add(b)
            edge[b].add(a)

        N = {i:e for i,e in enumerate(labels)}
        R = [0]*n

        def traverse(n):
            count = Counter()
            for e in edge[n]:
                edge[e].remove(n)
                count.update(traverse(e))
            count.update((N[n]))
            R[n] = count[N[n]]
            return count

        traverse(0)
        return R