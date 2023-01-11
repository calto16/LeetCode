class Solution(object):
    def minTime(self, n, edges, hasApple):
        graph = [[] for i in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(vertex, parent):
            time = 0
            for child in graph[vertex]:
                if(child != parent):
                    time += dfs(child, vertex)
            if((time>0 or hasApple[vertex]) and parent != -1):
                time += 2
            return time
        return dfs(0, -1)