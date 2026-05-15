# =====================================================================
#   1764번:    듣보잡
#   @date:   2026-02-15
#   @link:   https://www.acmicpc.net/problem/1764
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================
"""
그 사이에 있는 교집합을 구하라는 뜻이구나
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = set(input().strip() for _ in range(N))
B = set(input().strip() for _ in range(M))


check = A if len(A) < len(B) else B
room = A if check == B else B
cnt = 0
anw = []
for i in check:
    if i in room:
        cnt += 1
        anw.append(i)
print(cnt)
anw.sort()
for i in anw:
    print(i)
