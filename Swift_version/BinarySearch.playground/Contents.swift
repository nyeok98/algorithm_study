func binarySearch<T: Comparable>(array: [T], item[T]) -> Int {
    var low = 0
    var high = array.count - 1
    
    while low <= high {
        let mid = (low+high) / 2
        let target = array[mid]
        if target == item {
            return mid
        } else if target > mid {
            high = mid-1
        } else {
            low = mid+1
        }
    }
    
    return -1
}

var a = [1,2,3,45,5,8]
a.indices
