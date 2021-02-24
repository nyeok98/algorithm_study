#include "UsefulHeap.h"

void HeapInit(Heap *ph, PriorityComp pc){ // 힙의 초기화
    ph->numberOfData = 0;
    ph->comp = pc;
}

int HIsEmpty(Heap *ph){ // 힙이 비었는지 확인
    if (ph->numberOfData == 0) {
        return TRUE;
    } else {
        return FALSE;
    }
}

int GetParentIDX(int idx){ // 부모 노드의 인덱스 값 반환
    return idx/2;
}

int GetLChildIDX(int idx){ // 왼쪽 자식 노드의 인덱스 값 반환
    return idx*2;
}

int GetRChildIDX(int idx){ // 오른쪽 자식 노드의 인덱스 값 반환
    return GetLChildIDX(idx)+1;
}

// 두 개의 자식 노드 중 높은 우선순위의 자식 노드 인덱스 값 반환
int GetHiPriChildIDX(Heap *ph, int idx){
    if (GetLChildIDX(idx) > ph->numberOfData)
        return 0;
    else if (GetLChildIDX(idx) == ph->numberOfData)
        return GetLChildIDX(idx);
    else {
        if (ph->comp(ph->heapArr[GetLChildIDX(idx)], ph->heapArr[GetRChildIDX(idx)]) < 0)
            return GetRChildIDX(idx);
        else
            return GetLChildIDX(idx);
    }
}

// 힙에 데이터 저장
void HInsert(Heap *ph, HData data){
    int idx = ph->numberOfData+1;
    
    while(idx != 1){
        if (ph->comp(data, ph->heapArr[GetParentIDX(idx)]) > 0){
            ph->heapArr[idx] = ph->heapArr[GetParentIDX(idx)];
            idx = GetParentIDX(idx);
        } else
            break;
    }
    
    ph->heapArr[idx] = data;
    ph->numberOfData += 1;
}

// 힙에서 데이터 삭제
HData HDelete(Heap * ph){
    HData retData = ph->heapArr[1];
    HData lastElem = ph->heapArr[ph->numberOfData];
    
    int parentIdx = 1;
    int childIdx;
    
    while ((childIdx = GetHiPriChildIDX(ph, parentIdx))) {
        if (ph->comp(lastElem, ph->heapArr[childIdx]) >= 0)
            break;
        ph->heapArr[parentIdx] = ph->heapArr[childIdx];
        parentIdx = childIdx;
    }
    
    ph->heapArr[parentIdx] = lastElem;
    ph->numberOfData -= 1;
    
    return retData;
}
