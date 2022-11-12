# 까다로웠던 부분

### 17396
<img width="200" alt="image" src="https://user-images.githubusercontent.com/57023279/201478339-579b3757-fe28-4378-ad2f-722bc83ef1db.png">

보통 문제를 풀때 해당 간선까지 접근 불가한 경우 INF를 선언하고, 이때 INF는 10^9정도로 잡아둔다.</br>
17396의 경우는 정상적으로 최종 노드에 접근이 가능하더라도 N의 최댓값인 10만개의 노드 당 비용이 10만이라면</br>
result가 내가 자주쓰는 INF를 이미 초과하여 -1이 출력되며, 오답이다.</br>
인풋에 대한 엣지케이스에 더 신경써야하는 부분.

</br>

### 1504
<img width="344" alt="image" src="https://user-images.githubusercontent.com/57023279/201478503-909bcc8a-f599-42d4-b4b7-200138387e23.png">
간단하지만 모든 다익스트라 알고리즘에서 신경써야할 부분이다. </br>
출력값이 더해지다보면 INF 값을 초과할 수 있다.</br>
