def solution(n, paths, gates, summits):
    INF = int(1e9)

    graph = [[INF] * (n+1) for _ in range(n+1)]

    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    for path in paths:
        i, j, w = path
        graph[i][j] = w
        graph[j][i] = w

    for k in range(1, n+1):
        if k in summits:
            continue
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], max(graph[a][k], graph[k][b]))

    submit_intensity = []

    for summit in summits:
        for gate in gates:
            print(summit, gate)
            submit_intensity.append(
                [max(graph[gate][summit], graph[summit][gate]), summit])

    submit_intensity = sorted(submit_intensity)

    answer = [submit_intensity[0][1], submit_intensity[0][0]]

    return answer


print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [
      4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
