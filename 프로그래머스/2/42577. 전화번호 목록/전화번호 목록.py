def solution(phone_book):
    phone = {}
    
    for p in phone_book:
        if p not in phone:
            phone[p] = 1
    
    for p in phone_book:
        arr = ""
        for i in p:
            arr += i
            
            if arr in phone and arr != p:
                return False
    return True