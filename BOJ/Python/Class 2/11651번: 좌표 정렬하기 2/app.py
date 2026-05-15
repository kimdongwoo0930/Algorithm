# =====================================================================
#   11651번:    좌표 정렬하기 2
#   @date:   2026-02-03
#   @link:   https://www.acmicpc.net/problem/11651
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys

input = sys.stdin.readline
out = sys.stdout.write

N = int(input())
List = [tuple(map(int, input().split())) for _ in range(N)]

List = sorted(List, key=lambda x: (x[1], x[0]))
for i in List:
    out(str(i[0]) + " " + str(i[1]) + "\n")
