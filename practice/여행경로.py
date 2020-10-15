def solution(tickets):
    tree = {}
    for start, end in tickets:
        if start not in tree:
            tree[start] = [end]
        else:
            tree[start].append(end)

    for t in tree.keys():
        tree[t].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        cur = stack[-1]
        if cur not in tree or len(tree[cur]) == 0:
            path.append(stack.pop())
        else:
            stack.append(tree[cur][-1])
            tree[cur] = tree[cur][:-1]

    return path[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))