# =====================================================================
#   2798번:    블랙잭
#   @date:   2026-01-30
#   @link:   https://www.acmicpc.net/problem/2798
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""
이걸 3개씩 다뽑아서 검사를 하면 시간초과가 분명한데

맨뒤에껄 뽑아
while 리스트:
    리스트 원소가 3개인지 일단 검사
    그러고 맨뒤에꺼 뽑기
    for :
        뽑아 A + B + 나머지 한번씩 하고
        if N이랑 같으면 break
        else list 에 합 더하기 N보다 작아야함

ans = 0

while list:
    A = 9
    copy_list = nums
    B = 8
    for nums:
        if A + B + i == N:
            ans = N
            break
        if A + B + i <= N
            ans = max(N, A + B + i)
"""


import sys

input = sys.stdin.readline


N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

while nums:
    if len(nums) < 4:
        break
    A = nums.pop()  # -> 9
    copy_num = nums.copy()  # -> [5,6,7,8]
    while copy_num:  # - 2회차는 [5,6,7]
        if len(copy_num) < 2:
            break
        B = copy_num.pop()  # -> 8 -> 7
        for i in copy_num:
            if A + B + i == M:
                ans = M
                break
            elif A + B + i < M:
                ans = max(ans, A + B + i)

print(ans)
