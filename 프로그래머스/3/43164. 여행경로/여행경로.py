def solution(tickets):
    graph = dict()

    for s, e in tickets:
        if s not in graph:
            graph[s] = [e]
        else:
            graph[s].append(e)

    for g in graph:
        graph[g].sort()

    def dfs(airport, path):
        if len(path) == len(tickets) + 1:
            return path[:]

        if airport not in graph:
            return None

        for i in range(len(graph[airport])):
            next_airport = graph[airport].pop(i)

            path.append(next_airport)

            result = dfs(next_airport, path)
            if result:
                return result

            path.pop()
            graph[airport].insert(i, next_airport)

        return None

    return dfs("ICN", ["ICN"])