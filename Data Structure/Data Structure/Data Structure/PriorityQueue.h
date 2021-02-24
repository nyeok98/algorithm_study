#ifndef PriorityQueue_h
#define PriorityQueue_h

#include "UsefulHeap.h"

typedef Heap PQueue;
typedef HData PQData;

void PQueueInit(PQueue *ppq, PriorityComp pc);
int PQIsEmpty(PQueue *ppq);

void PEnqueue(PQueue *ppq, PQData data);
PQData PDequeue(PQueue *ppq);

#endif /* PriorityQueue_h */
