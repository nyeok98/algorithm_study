import Foundation

let INF = Int.max

let n = Int(readLine()!)!
let m = Int(readLine()!)!
var connection = [[Int]]()
let distance = [Bool](repeating: false, count: n+1)

for _ in 0...m {
    let info = readLine()!.split(separator: " ").map({Int($0)})
    connection[info[0]!].append(info[1]!)
    connection[info[0]!].append(info[2]!)
}

let points = readLine()!.split(separator: " ").map({Int($0)})
let start = points[0]!
let end = points[1]!

