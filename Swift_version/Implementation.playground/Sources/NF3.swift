import Foundation

func solution(_ games:[[Int]]) -> Int {
    var discountedGameIdx = [Int]()
    var table = [[(Int, Int)]](repeating: [], count: games.count)
    var dummy = [Int]()
    for (count, game) in games.enumerated() {
        table[game[1]].append((game[0]*game[2]/100, count))
    }
    let emptyDay = countEmptyDay(table)

    for day in table {
        if day.isEmpty { continue }
        var maxVal = day[0].0 // 최대할인률을 갖는 게임의 할인값
        var maxI = day[0].1 // 최대할인률을 갖는 게임의 인덱스
        for tuple in day {
            if tuple.0 > maxVal {
                dummy.append(maxVal)
                maxVal = tuple.0
                maxI = tuple.1
            } else {
                dummy.append(tuple.0)
            }
        }
        discountedGameIdx.append(maxI)
    }

    var total = 0

    for (i, game) in games.enumerated() {
        if discountedGameIdx.contains(i) { // 할인을 적용할 수 있는 게임
            total += game[0] * (100-game[2]) / 100
        } else { // 할인이 적용되지 않는 게임
            total += game[0]
        }
    }

    if emptyDay > 0 { // 뒤에서부터 할인이 연속적으로 없는 날은 앞에서 할인하는 날에 살 수 있으므로
        dummy.sort(by: >)
        for i in 0..<emptyDay {
            total -= dummy[i]
        }
    }

    return total
}

func countEmptyDay(_ table:[[(Int, Int)]]) -> Int {
    var max = 0
    for day in table.reversed() {
        if day.isEmpty {
            max += 1
        } else { break }
    }
    return max // 뒤에서 부터 할인 아이템이 전혀 없는 일수를 확인
}
