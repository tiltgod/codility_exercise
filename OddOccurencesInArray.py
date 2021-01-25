def solution(A):
    for i in range(len(A)):
        ans = 0
        for i in A:
            ans ^= i
        return ans
        