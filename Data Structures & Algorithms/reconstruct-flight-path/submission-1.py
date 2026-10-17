class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}

        for src, dst in sorted(tickets, reverse=True):
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)

        res = []

        def dfs(src):
            while src in adj and adj[src]:
                v = adj[src].pop()
                dfs(v)

            res.append(src)

        dfs("JFK")
        return res[::-1]