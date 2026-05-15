# =====================================================================
#   1966번:    프린터 큐
#   @date:   2026-02-06
#   @link:   https://www.acmicpc.net/problem/1966
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================


"""
중요도에 따라 문제가 몇번째에 인쇄가능한지 물어보는거잖아
입력 1 -> 테스트 케이스 횟수
입력 2 -> N, M. N 은 문서 개수 / M 은 순서가 궁금한  문서가 que에 몇번째에 있는지
입력 3 -> 중요도
A B C D
1 2 3 4

어떻게 찾을까
먼저 찾아야하는 숫자를 정해두고
그러고 높은순으로 정렬해야하나
내가 처음 생각한건 이게 큐문제니까
앞에서부터 하나 빼서 검사하는데 얘보다 큰놈이 있으면 맨뒤로 다시넣고 하는걸 원했지
그때 제일큰놈이 없을때 그놈이 원하느놈일때까지 센 cnt 가 답인거지


"""

import sys
from collections import deque

input = sys.stdin.readline


A = int(input())
for _ in range(A):
    N, M = map(int, input().split())
    List = list(map(int, input().split()))
    # 4, 2 들어오면 3번째를 찾아달라는거니까
    # 숫자들의 3번째를 찾아서 몇번째인지 찾아야겠네
    # 그냥 큐로 하자 굳이 dict까지 할 필요없을듯
    Room = deque([i, List[i]] for i in range(N))
    find = M
    # 이제 앞에서부터
    cnt = 1
    while True:
        # 리스트 맨앞에서부터 가장높은걸 찾아야한다.
        A = Room.popleft()
        # 먼저 find 인지 아닌지가 중요할듯
        # 그리고 구분해야할듯

        if A[1] != max(List):
            Room.append(A)
        else:
            if A[0] == find:
                break
            else:
                List.remove(A[1])
                cnt += 1

    print(cnt)
