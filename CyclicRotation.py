from collections import deque

def solution(A, K):
    # write your code in Python 3.6
    Adeq = deque(A)
    for i in range(K):
        x = Adeq.pop()
        Adeq.appendleft(x)
    return list(Adeq)
    pass
