#=====================================================================
#   9095번:    1, 2, 3 더하기                   
#   @date:   2026-02-24              
#   @link:   https://www.acmicpc.net/problem/9095  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

#DP 문제
# DP : 계산값을 저장후 재활용하기 

# T의 케이스 개수
# 각 숫자가 1 2 3으로 어케 이루어지는지 경우의 수를 구하는거다.


import sys;

input = sys.stdin.readline

T = int(input())


dp = [1,2,4]

Input = list(int(input()) for _ in range(T))
M = max(Input)
for i in range(3,M):
    dp.append(dp[i-3] + dp[i-2] + dp[i-1])

for i in Input:
    print(dp[i-1])
    

