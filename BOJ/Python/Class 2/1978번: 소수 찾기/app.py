# =====================================================================
#   1978번:    소수 찾기
#   @date:   2026-01-29
#   @link:   https://www.acmicpc.net/problem/1978
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys

input = sys.stdin.readline

cnt = 0


N = int(input())
List = list(map(int, input().split()))
for i in List:
    if i < 2:
        continue
    elif i == 2:
        cnt += 1
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        cnt += 1
print(cnt)
