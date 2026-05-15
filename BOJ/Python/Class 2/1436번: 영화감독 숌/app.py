# =====================================================================
#   1436번:    영화감독 숌
#   @date:   2026-02-02
#   @link:   https://www.acmicpc.net/problem/1436
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================
"""
문자에 666이 들어가면서 나올 껄 세야하네
"""


import sys

input = sys.stdin.readline
N = int(input())

num = 666
cnt = 0

while True:
    if "666" in str(num):
        cnt += 1
        if cnt == N:
            print(num)
            break
    num += 1
