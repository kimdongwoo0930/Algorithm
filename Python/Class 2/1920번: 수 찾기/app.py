# =====================================================================
#   1920번:    수 찾기
#   @date:   2026-02-03
#   @link:   https://www.acmicpc.net/problem/1920
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""
N을 입력받아 a 라는 list를  만들고
m 을 입력받아 m번 입력받으면서 a에 있으면 1 없으면 0을 넣자
"""
import sys

input = sys.stdin.readline
out = sys.stdout.write

N = input()
List = set(map(int, input().split()))
M = input()
B = map(int, input().split())
ㅇ
for i in B:
    if i in List:
        out(str(1) + "\n")
    else:
        out(str(0) + "\n")
