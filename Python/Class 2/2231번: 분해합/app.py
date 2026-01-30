# =====================================================================
#   2231번:    분해합
#   @date:   2026-01-30
#   @link:   https://www.acmicpc.net/problem/2231
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================


"""
음 N까지 반복을 해서 찾아서 나오는 순간 출력하는게 촤소값이자나
"""
import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    Sum = 0
    List = list(str(i).strip())
    for j in List:
        Sum += int(j)
    if i + Sum == N:
        print(i)
        break
    elif i == N - 1:
        print(0)
