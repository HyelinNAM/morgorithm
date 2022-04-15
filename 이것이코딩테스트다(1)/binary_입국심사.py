def solution(n, times):
    
    # array ) 0 ~ max(times)
    start = 0
    end = max(times) * n
    answer = 0
    
    while start <= end:
        mid = (start+end) // 2
        people = sum([mid//t for t in times])

        if people < n: # 처리해야하는 사람보다 더 적은 사람 처리 > 시간 늘리자
            start = mid + 1
        
        else: # 처리해야하는 사람보다 더 많은 사람 처리
            answer = mid
            end = mid - 1

    return answer

solution(4,[1,1,1])
