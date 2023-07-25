"""
가장 큰 수
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
"""

from functools import cmp_to_key

def compare_str(a,b):
    sum1 = a + b
    sum2 = b + a

    if int(sum1) > int(sum2):
        return 1
    elif int(sum2) > int(sum1):
        return -1
    else:
        return 0

def solution(numbers):
    str_numbers = [str(x) for x in numbers]
    str_numbers.sort(key=cmp_to_key(compare_str), reverse=True)
    answer = str(int("".join(str_numbers)))
    return answer
