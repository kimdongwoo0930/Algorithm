# =====================================================================
#   1259번:    팰린드롬수
#   @date:   2026-01-30
#   @link:   https://www.acmicpc.net/problem/1259
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys

input = sys.stdin.readline


while 1:
    N = int(input())
    result = "yes"
    if N == 0:
        break
    nums = list(map(int, str(N).strip()))
    for i in range(len(nums) // 2 + 1):
        if nums[i] != nums[-i - 1]:
            result = "no"
            break
    print(result)
