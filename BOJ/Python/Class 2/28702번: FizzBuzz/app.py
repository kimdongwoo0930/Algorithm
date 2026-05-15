# =====================================================================
#   28702번:    FizzBuzz
#   @date:   2026-02-02
#   @link:   https://www.acmicpc.net/problem/28702
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""
3의 배수 and 5의 배수 => FizzBuzz
3의 배수 => Fizz
5의 배수 => Buzz
not 3의 배수 and not 5의 배수 => i

아이디어:
    숫자만 여러개 올수도 있고
    문자만 여러개 올수도 있다.


    Fizz Buzz 11 ->. 9 10 11 -> 12 = Fizz

    1 2 Fizz -> 4

    숫자만 있을 경우 그 숫자를 기준으로 하면되지만
    숫자가 없을경우 문자들이 존재할만한 부분을 찾아야한다.
    입력은 무조건 3개로 들어오고 다음 나올 숫자또는 문자열을 출력하면 된다.

    숫자인경우 그냥 인덱스를 찾아서 + 남은 인덱스 해주고
    거기에 맞는 문자열을 내면된다.

ex)
    Fizz.   1 x 3 , 2 x 3 ... (3 x 3 + 1) % 5
    Buzz   만약 위에 조건에 맞는 숫자가 나왔을때 또 반복시작해서
    FizzBuzz
    =>.

"""


def check_ans(X):
    if X % 3 == 0 and X % 5 == 0:
        return "FizzBuzz"
    elif X % 3 == 0:
        return "Fizz"
    elif X % 5 == 0:
        return "Buzz"
    else:
        return str(X)


import sys

input = sys.stdin.readline
out = sys.stdout.write
result = 0
# 먼저 숫자가 포함된경우를 만들어 볼까?
# 아니면 문자열도 어떻게 처리해야하는지 생각부터해보자

List = list(input().strip() for _ in range(3))
for i in List:
    # isdigit() -> 숫자인지 문자인지 확인용
    if i.isdigit():
        # 숫자 현재 인덱스를 찾아  2에서 뺴고 1더하면 그 숫자이니 3 - i 를합시다
        x = List.index(i)
        X = int(i) + (3 - x)
        result = check_ans(X)
        break
# if result == 0:
#     first = List[0]
#     second = List[1]
#     for i in range(1, 1000001):
#         # 먼저 3 5 3,5인지 확인하고 1번 2번의  조건의 맞는 숫자를 구하고
#         # 그다음 3번째 숫자까지 비교해서 맞는 숫자를 찾는다.
#         if first == "Fizz":
#             (i * 3)

print(result)
