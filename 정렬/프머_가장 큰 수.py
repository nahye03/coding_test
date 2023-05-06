def solution(numbers):
    num_str = list(map(str, numbers))
    # 문자열은 숫자 비교할때 한자리씩 비교하기 때문에 가능
    num_str.sort(key=lambda x:x*3, reverse=True)
    answer = str(int(''.join(num_str)))

    return answer

###다른 풀이
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    if t1>t2:
        return -1
    elif t1<t2:
        return 1
    else:
        return 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n.sort(key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer