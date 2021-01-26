# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    step = 0
    dis = Y - X
    if dis == 0:
        return step
    else:
        if D > dis:
            step = 1
        else:
            if dis % D == 0:
                step = int(dis / D)
            else:
                step = dis // D + 1
    return step
    pass