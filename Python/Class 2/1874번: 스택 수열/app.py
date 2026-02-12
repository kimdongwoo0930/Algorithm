# =====================================================================
#   1874번:    스택 수열
#   @date:   2026-02-06
#   @link:   https://www.acmicpc.net/problem/1874
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================
"""
1  부터 n 까지의
n 개의 줄의 수열을 이루는 n개의 정수가 들어온다.
스택에 push하느 순서는 반드시 오름차순을 지킨다.
아 숫자를 한번에 받아서 거기서부터 이제 오름차순으로 계산하는거야?

아 이 있는 stack에서 어케 저 번호대로 뽑냐 이거구나 ㅇㅋ


[ 1, 2, 3, 4, 5, 6, 7, 8]
4, 3, 6, 8 /....
push push push push pop
if index - 1
[1 , 2, 3, 5, 6, 7, 8]
-1 햇을 index가 내가 찾던거면  pop 아또면 또 올라가야지
그러고 뽑으면 일단 전꺼 검사 그러고 또 올라가
"""


import sys

input = sys.stdin.readline

N = int(input())
stack = [i + 1 for i in range(N)]
ans = []
index = 0
try:
    for _ in range(N):
        A = int(input())
        # 첫번째 숫자를 찾아ㅑ하니
        #  stack 반복을시작해야지
        # 반복을 계속 돌리긴한데 이제 index를 기억해야한다
        while True:
            if index == 0:
                ans.append("+")
                index += 1
                continue
            elif stack[index - 1] == A:
                stack.pop(index - 1)
                ans.append("-")
                index -= 1
                break
            else:
                ans.append("+")
                index += 1
    print(" ".join(ans))
except:
    print("NO")
