def solution(N):
    n_list = list("{:b}".format(N))
    gaps = 0
    temp = 0
    if all(x == 0 for x in n_list[1:]):
        return gaps

    for i in n_list[1:]:
        if i == '0':
            temp += 1
        else:
            if temp > gaps:
                gaps = temp
            temp = 0
    return gaps
    pass
