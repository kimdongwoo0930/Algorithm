# =====================================================================
#   11723번:    집합
#   @date:   2026-02-15
#   @link:   https://www.acmicpc.net/problem/11723
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================


"""
집합하나를 만든다.
add 일경우 집합에 추가하기 ( 이미 존재할경우 무시 )
remove 일경우 집합 S에서 X를 제거
check 일경우 숫자가 있으면 1 없으면 0을 출력한다.
toggle 만약 x가 있다면 x를 제거 없다면 추가한다
all 일경우 {1,2,.... 20} 으로 변경한다.
empty 일경우 집합을 비운다.
"""

import sys

input = sys.stdin.readline

N = int(input())
S = set()
for _ in range(N):
    # 입력을 먼저받아서 그게 머가 들어있느지 확인하자
    Input = input().strip()
    if "add" in Input:
        num = int(Input.split()[1])
        S.add(num)
    elif "remove" in Input:
        num = int(Input.split()[1])
        if num in S:
            S.remove(num)
    elif "check" in Input:
        num = int(Input.split()[1])
        if num in S:
            print(1)
        else:
            print(0)
    elif "toggle" in Input:
        num = int(Input.split()[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif "all" in Input:
        List = [i for i in range(1, 21)]
        S = set(List)
    elif "empty" in Input:
        S.clear()
