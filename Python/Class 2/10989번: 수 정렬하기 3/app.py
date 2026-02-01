# =====================================================================
#   10989번:    수 정렬하기 3
#   @date:   2026-02-01
#   @link:   https://www.acmicpc.net/problem/10989
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================
"""

1. list을 매번 추가하면 결국 메모리 초과가 뜬다.
2. 시간초과가 아니기때문에 반복은 해도 된다.
3. sys.stdout.write 사용해서 시간을 더 줄인다.
4. 미리 최대치인 100001개만큼 생성을 해두고 나온숫자 의 개수를 늘린다.

5. 메모리 초과가 왜뜨는데 씨바

"""
import sys

input = sys.stdin.readline
out = sys.stdout.write

N = int(input())
List = [0] * 10001
for i in range(N):
    List[int(input())] += 1


for i in range(1, 10001):
    if List[i] != 0:
        for _ in range(List[i]):
            out(str(i) + "\n")
