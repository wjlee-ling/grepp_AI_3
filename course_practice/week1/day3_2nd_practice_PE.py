"""
체육복: greedy algorithm
첫 코드에 문제점: 여분이 있는 사람이 본인의 것을 잃어버리면 빌려주지 못한다는 점을 제대로 처리 못함.
수정사항:
1) i가 여분이 있고, lost에 포함되어 있는데, (i보다 arr에 먼저 포함된) i-1 또는 i+1인 사람이 i의 것을 가져가는 경우를 고침
2) 주어진 lost, reserve의 class를 list에서 set로 바꿈으로써: remove와 in 작업의 시간 복잡도를 O(n) 에서 (평균) O(1)로 줄임
"""
def solution(n, lost, reserve):
    reserve.sort()
    lost, reserve = map(set, [lost, reserve])
    own = lost & reserve # 여분이 있는 사람이 체육복을 잃어버렸을 때
    lend = reserve - own # 여분이 있는 사람들 중 빌려줄 수 있는 학생
    lend.sort()

    for l in (lost-own): # lost-own (own인 애들은 여분을 입으면 되니)
        if l-1 in lend:
            lend.remove(l-1)
        elif l+1 in lend:
            lend.remove(l+1)
    answer = n - len(lost) +len(reserve) -len(lend)
    return answer
