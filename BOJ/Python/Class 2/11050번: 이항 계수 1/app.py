# =====================================================================
#   11050번:    이항 계수 1
#   @date:   2026-02-01
#   @link:   https://www.acmicpc.net/problem/11050
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""

이항계수

(n)  ->  n(n-1)(n-2) ... (n-k+1)  -> n!
(k)  ->  k!                       -> k!(n-k)!
"""


import sys
import math

input = sys.stdin.readline
out = sys.stdout.write


N, K = map(int, input().split())

n = math.factorial(N)
k = math.factorial(K) * math.factorial(N - K)


out(str(n // k))
