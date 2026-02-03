# =====================================================================
#   1676번:    팩토리얼 0의 개수
#   @date:   2026-02-03
#   @link:   https://www.acmicpc.net/problem/1676
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""
n! 에서 뒤에서 부터 처음 0이아닌 숫자가 나올떄 까지?

10! => 3628800.  008 나오면 끝
6 2 1
"""


import sys
import math

input = sys.stdin.readline

# 입려받기
N = int(input())
# N! 구하기
N = math.factorial(N)
# N! 한자리씩 다 문자열로 나누기
nums = list(str(N).strip())
nums.reverse()
# 0이 안나올때까지 cnt하기
cnt = 0
for i in nums:
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)
