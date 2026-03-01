# =====================================================================
#   11399번:    ATM
#   @date:   2026-02-24
#   @link:   https://www.acmicpc.net/problem/11399
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================


# 이거 그냥 간짧은사람이 앞에서부터 하는게 맞지않냐

import sys

input = sys.stdin.readline

N = int(input())
List = list(map(int, input().split()))

time = 0
ans = 0
for i in sorted(List):
    ans += time + i
    time += i

print(ans)

# 1 + 3 + 6 + 9 + 13 +  =>
