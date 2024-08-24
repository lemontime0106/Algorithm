def solution(elements):
    answer = 0
    n = len(elements)
    numbers = set()
    
    circular_elements = elements * 2
    
    for i in range(1, n+1):
        for j in range(n):
            numbers.add(sum(circular_elements[j:j+i]))
    
    answer = len(numbers)
    return answer
