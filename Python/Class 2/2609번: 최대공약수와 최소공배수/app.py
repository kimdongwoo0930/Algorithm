# =====================================================================
#   2609번:    최대공약수와 최소공배수
#   @date:   2026-01-30
#   @link:   https://www.acmicpc.net/problem/2609
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys
import math

input = sys.stdin.readline

A, B = map(int, input().split())


max_num = math.gcd(A, B)  # 최대공약수
min_num = math.lcm(A, B)  # 최소공배수

print(max_num, min_num)
