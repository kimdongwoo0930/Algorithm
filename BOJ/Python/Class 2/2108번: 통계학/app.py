# =====================================================================
#   2108번:    통계학
#   @date:   2026-02-11
#   @link:   https://www.acmicpc.net/problem/2108
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================
"""
1. 산술평균 구하기
2. 중앙값 구하기
3. 최빈값 구하기
4. 범위 구하기

N 이 입력되면 N개만큼 받기
숫자 5개 받아서
4가지 계산하기
"""
import sys

input = sys.stdin.readline

N = int(input())
Input = list(int(input()) for _ in range(N))
avg = sum(Input) / N

one = int(avg + 0.5) if avg >= 0 else int(avg - 0.5)
List = Input.copy()
List.sort()
center = (len(List) + 1) // 2
two = List[center - 1]
Dict = {i: 0 for i in Input}
for i in Input:
    Dict[i] += 1

max_cnt = max(Dict.values())
modes = [k for k, v in Dict.items() if v == max_cnt]
modes.sort()
three = modes[0] if len(modes) == 1 else modes[1]
four = max(Input) - min(Input)

print(one)
print(two)
print(three)
print(four)
