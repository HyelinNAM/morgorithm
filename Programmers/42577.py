def solution(phone_book):
    
    answer = True
    
    phone_dict = {p:1 for p in phone_book}
    
    for phone in phone_book:
        for i in range(len(phone)-1):
            if phone_dict.get(phone[:i+1]):
                answer = False
                break
        
        if not answer:
            break
    
    return answer