def solution(number, k):
    answer = []

    for n in number:
        if not answer:
            answer.append(n)
            continue
        if k > 0:
            while answer[-1] < n:
                answer.pop()
                k -= 1
                if k == 0 or not answer:
                    break
        answer.append(n)

    return ''.join(answer[:len(number) - k])

###다른 풀이
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)