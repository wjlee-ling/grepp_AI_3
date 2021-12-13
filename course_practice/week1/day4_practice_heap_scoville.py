"""
다음 공식에 따라 주어진 리스트의 모든 원소가 주어진 K보다 높게끔 만드는 작업의 최소 시도값을 구하는 문제
공식: (smallest) + (2nd_smallest) * 2 ==> new element

<ver1>
문제점: 정확성은 100 퍼센트 통과이나, 효율성 검사를 통과하지 못함.
"""

def heapify(unsorted, i, heap_size):
    biggest = i
    left, right = 2 * i, 2*i + 1
    if left < heap_size and unsorted[left] < unsorted[biggest]:
        biggest = left
    if right < heap_size and unsorted[right] < unsorted[biggest]:
        biggest = right
    if biggest != i:
        unsorted[biggest], unsorted[i] = unsorted[i], unsorted[biggest]
        heapify(unsorted, biggest, heap_size)

def heap_sort(unsorted):
    # 여기서 sort란 리스트가 처음부터 끝까지 오름차순이라는 것이 아니라
    # 모든 sub-tree가 mean-heap-binary-tree의 조건을 만족한다는 의미
    n = len(unsorted)
    for i in range(n//2, 0, -1):
        # 잎새노드들은 할 필요가 없고 + 자식이 있는 노드부터 하면 됨
        heapify(unsorted, i, n)

def solution(scoville, K):
    count = 0
    scoville = [None] + scoville # heap tree의 index를 맞추기 위해
    while len(scoville) >=3:
    # 아래 코드가 가능한 최소 환경이 [None, smallest, next_smallest]
        heap_sort(scoville)
        scoville[1], scoville[-1] = scoville[-1], scoville[1]
        smallest = scoville.pop()

        # 성공조건: 모두 다 K 이상
        if smallest >= K:
            break

        heap_sort(scoville)
        scoville[1], scoville[-1] = scoville[-1], scoville[1]
        next_smallest = scoville.pop()
        #print(smallest, next_smallest)
        new = smallest + (next_smallest *2)
        scoville.append(new)
        count += 1
        
    if scoville[-1] < K:
    # 원래 [None, N] 에서 ind_N == 1 and N <K이거나, 윗 과정을 거쳐도 마지막 요소가 K 미만일
        return -1

    return count
