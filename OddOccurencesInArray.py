def solution(A):
    for i in range(len(A)):
        ls = A.copy()
        ls.pop(i)
        if A[i] in ls:
            pass
        else:
            return A[i] 
        