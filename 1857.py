# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # INF = float('inf')
        # n = len(colors)
        # adj = defaultdict(list)
        # for u, v in edges:
        #     adj[u].append(v)
        # count = [[0]*26 for _ in range(n)]
        # vis = [0]*n
        
        # def dfs(node):
        #     if vis[node] == 1:
        #         return INF   
        #     if vis[node] == 2:
        #         return count[node][ord(colors[node]) - ord('a')]
            
        #     vis[node] = 1
        #     for nxt in adj[node]:
        #         res = dfs(nxt)
        #         if res == INF:
        #             return INF
        #         for c in range(26):
        #             count[node][c] = max(count[node][c], count[nxt][c])
            
        #     col = ord(colors[node]) - ord('a')
        #     count[node][col] += 1
        #     vis[node] = 2  
            
        #     return count[node][col]
        # ans = 0
        # for i in range(n):
        #     val = dfs(i)
        #     if val == INF:
        #         return -1
        #     ans = max(ans, val)
        
        # return ans
        queue = deque()
        dic = {}
        n = len(colors)
        indegree = [0] * n
        count = [{} for _ in range(n)]
        max_count = 0

        for x, y in edges:
            if y in dic:
                dic[y].append(x)
            else:
                dic[y] = [x]
            indegree[x] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            cur = queue.popleft()
            
            color = colors[cur]
            if color in count[cur]:
                count[cur][color] += 1
            else:
                count[cur][color] = 1
            max_count = max(max_count, count[cur][color])
            if cur in dic:
                for neighbor in dic[cur]:
                    for key, val in count[cur].items():
                        if key in count[neighbor]:
                            count[neighbor][key] = max(val, count[neighbor][key])
                        else:
                            count[neighbor][key] = val
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        
        for i in indegree:
            if i != 0:
                return -1
        return max_count
