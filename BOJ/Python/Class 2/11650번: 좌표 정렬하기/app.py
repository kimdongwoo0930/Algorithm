# =====================================================================
#   11650번:    좌표 정렬하기
#   @date:   2026-02-03
#   @link:   https://www.acmicpc.net/problem/11650
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""

자 보자 모두 입력받아서 x좌표순으로 정렬한다 그러고 그중 x가 같으면 y좌표로 비교한다.
N으로 문자를 받고
x좌표 기준으로 정렬하고
반복하면서 x가 같은애들끼리 중에 y좌표로 정렬후 출력

"""


import sys

input = sys.stdin.readline
out = sys.stdout.write

N = int(input())
List = [tuple(map(int, input().split())) for _ in range(N)]

List = sorted(List)
for i in List:
    out(str(i[0]) + " " + str(i[1]) + "\n")
