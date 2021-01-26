def solution(A):
    # write your code in Python 2.7
    sum = 0
    N = len(A)
    for val in A:
        sum += val

    expected = (N + 1) * (N + 2) // 2;