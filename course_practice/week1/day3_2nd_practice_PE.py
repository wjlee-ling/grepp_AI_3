"""
체육복: greedy algorithm
"""
def solution(n, lost, reserve):
    remove_n = len(reserve)
    reserve.sort()
    for l in lost:
        if l in reserve:
            reserve.remove(l)
        elif l-1 in reserve:
            reserve.remove(l-1)
        elif l+1 in reserve:
            reserve.remove(l+1)
    remove_n -= len(reserve) # saved
    answer = n - len(lost) + remove_n

    return answer
