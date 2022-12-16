var visited = [Bool](repeating: false, count: 9)
var q = [Int]()

func bfs(start: Int) {
    q.append(start)
    visited[start] = true
    
    while !q.isEmpty {
        let a = q.removeFirst()
        print(a, terminator: " ")
        for i in connection[a] {
            if !visited[i] {
                q.append(i)
                visited[i] = true
            }
        }
    }
}

let connection = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

bfs(start: 1)
