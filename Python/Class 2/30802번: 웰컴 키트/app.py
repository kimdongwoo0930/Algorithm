#=====================================================================
#   30802번:    웰컴 키트                   
#   @date:   2026-01-29              
#   @link:   https://www.acmicpc.net/problem/30802  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

N = int(input())
Size = list(map(int, input().split()))
T, P = map(int, input().split())

S_result = 0


for i in Size:
    if i % T == 0:
        S_result += (i//T)
    else:

        S_result += (i//T + 1)
print(S_result)
print("{} {}".format(N//P, N%P))