import Foundation
var result = 0
let table = [[(33000, 0)], [], [(1600, 1), (4125, 3)], [(16900, 2)]]

for day in table {
    result += min(day[0], day[day.count-1])
}

print(result)
