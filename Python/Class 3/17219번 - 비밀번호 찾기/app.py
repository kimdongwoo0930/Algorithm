# =====================================================================
#   17219번:    비밀번호 찾기
#   @date:   2026-02-24
#   @link:   https://www.acmicpc.net/problem/17219
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

# 주소의 개수 N
# 비밀번호 찾으러는 수 M
# 다 입력받고 마지막에 그냥 나온거 꺼내주면된다.

import sys

input = sys.stdin.readline


N, M = map(int, input().split())
List = {}
for _ in range(N):
    juso, pwd = map(str, input().split())
    List[juso] = pwd

for _ in range(M):
    juso = input().strip()
    print(List[juso])
