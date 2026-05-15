# =====================================================================
#   2751번:    수 정렬하기 2
#   @date:   2026-02-03
#   @link:   https://www.acmicpc.net/problem/2751
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""
N을 받아 그럼 N개의 숫자를 받는다.
! 수는 중복할수 없다.
이걸 그냐 sort하면 메모리 초과나 시간초과뜰려나
일단 구현해보자
"""


import sys

input = sys.stdin.readline
out = sys.stdout.write

N = int(input())

List = list(int(input()) for _ in range(N))
List.sort()
for i in List:
    out(str(i) + "\n")
