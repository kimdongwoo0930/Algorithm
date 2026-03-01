# =====================================================================
#   11047번:    동전 0
#   @date:   2026-02-24
#   @link:   https://www.acmicpc.net/problem/11047
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

# 그리다: 동전의 가치가 큰거부터 나열
# 동전의 개수들을 위에서부터 나눠서 가져가면 그게 제일 작은 개수이다.

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(int(input().strip()) for _ in range(N))

coin = 0
last = K

for i in reversed(coins):
    if last < i :
        continue
    coin += last // i
    last =  last % i
    if last == 0:
        break

print(coin)
