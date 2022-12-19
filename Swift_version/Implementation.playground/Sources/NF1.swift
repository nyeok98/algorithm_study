import Foundation

func solution(_ a:[Int64]) -> Int64 {
    var sortedA = a
    sortedA.sort()
    var solution: Int64 = 0
    var start = 0
    var end = sortedA.count - 1
    let mid = (start+end)/2
    if end%2 + 1 == 1 { solution += sortedA[mid] }

    while start < end {
        solution += sortedA[end]
        end -= 1
        solution -= sortedA[start]
        start += 1
    }

    return solution
}
