#=====================================================================
#   22993번:    서든어택 3                   
#   @date:   2026-04-08              
#   @link:   https://www.acmicpc.net/problem/22993  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

power = A[0]
for enemy in sorted(A[1:]):
    if power <= enemy:
        print("No")
        break
    power += enemy
else:
    print("Yes")
