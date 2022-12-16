import Foundation

// T는 비교 가능해야 하기 때문에 Comparable을 준수해야함
struct Heap<T: Comparable> {
    // 실제 힙을 저장하는 장소
    var nodes: [T] = []
    private let sort: (T, T) -> Bool
    
    init(sort: @escaping (T, T) -> Bool) {
        self.sort = sort
    }
    
    // MARK: Insert, Delete
    
    // struct이기 때문에 data를 insert하면 현재 값타입을
    // 새로운 값타입으로 다시 그리기 때문에 mutating 키워드를 써야한다.
    mutating func shiftUp(child: Int) {
        var child = child
        var parent = parentIndex(of: child)
        
        // 노드의 제일 위까지 올라가거나, 부모의 노드 값과 비교했을 때 자기 자리일 때
        while child > 0 && sort(nodes[child], nodes[parent]) {
            nodes.swapAt(child, parent)
            child = parent
            parent = parentIndex(of: child)
        }
    }
    
    mutating func shiftDown(parent: Int) {
        var parent = parent
        
        while true {
            let left = leftChildIndex(of: parent)
            let right = rightChildIndex(of: parent)
            var candidate = parent
            if left < nodes.count && sort(nodes[left], nodes[candidate]) {
                candidate = left
            }
            
            if right < nodes.count && sort(nodes[right], nodes[candidate]) {
                candidate = right
            }
            
            if candidate == parent {
                return
            }
            nodes.swapAt(parent, candidate)
            parent = candidate
        }
        
    }
    
    mutating func insert(_ data: T) {
        nodes.append(data)
        let lastIndex = nodes.count - 1
        shiftUp(child: lastIndex)
    }
    
    mutating func remove() -> T? {
        guard !nodes.isEmpty else { return nil }
        
        nodes.swapAt(0, nodes.count - 1)
        
        defer { shiftDown(parent: 0) }
        
        return nodes.removeLast()
    }
    
    mutating func remove(at index: Int) -> T? {
        guard index < nodes.count else { return nil }
        
        if index == nodes.count - 1 {
            return nodes.removeLast()
        } else {
            nodes.swapAt(index, nodes.count - 1)
            
            defer {
                shiftUp(child: index)
                shiftDown(parent: index)
            }
            
            return nodes.removeLast()
        }
    }
    
    public func peek() -> T? {
        return nodes.first
    }
    
    // MARK: Private Methods
    
    private func parentIndex(of child: Int) -> Int {
        return (child - 1) / 2
    }
    
    private func leftChildIndex(of parent: Int) -> Int {
        return (parent * 2) + 1
    }
    
    private func rightChildIndex(of parent: Int) -> Int {
        return parent * 2
    }
}
