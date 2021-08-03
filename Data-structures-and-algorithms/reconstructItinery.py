input = [["JFK","SFO"], ["JFK","ATL"], ["SFO","ATL"],["ATL","SFO"]]
adj = {}

def findItinerary(input):
    for s in input:
        adj[s[0]] = []
        adj[s[1]] = []

    for s in input:
        adj[s[0]].append(s[1])

    for i in adj.values():
        i.sort()

    output = []
    def helper(node):
        while adj[node]:
            helper(adj[node].pop(0))
        output.append(node)
    helper("JFK")
    return (reversed(output))

# if __name__ == "__main__":
#     assert findItinerary(input) == ['JFK', 'SFO', 'ATL', 'SFO', 'ATL'], "Test case failed."
