#lv2 기능개발
# solution 1
def solution(progresses, speeds):
    from math import ceil
    answer = []
    work_days = []
    for p, s in zip(progresses, speeds):
        remaining = 100-p
        work_days.append(ceil(remaining/s))
    for day in work_days:
        try:
            if prev < day:
                answer.append(cum_sum)
                prev = day
                cum_sum = 1
            else:
                cum_sum += 1
        except:
            #1st element
            prev = day
            cum_sum =1
    answer.append(cum_sum)
    return answer

# solution2
def solution(progresses, speeds):
    from math import ceil
    answer = []
    work_days = []
    for p, s in zip(progresses, speeds):
        remaining = 100-p
        work_days.append(ceil(remaining/s))
    cum_sum = 0
    prev = work_days[0]
    work_days.append(100) # to return the result of the last element
    while work_days:
        curr = work_days.pop(0)
        if prev >= curr:
            cum_sum +=1
        else:
            answer.append(cum_sum)
            cum_sum = 1
            prev = curr
    return answer
