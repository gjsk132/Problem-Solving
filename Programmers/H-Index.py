def solution(citations):
    
    citations.sort(reverse = True)
    
    max_h = 0
    
    for i, c in enumerate(citations):
        if c >= i+1:
            max_h = i+1
    
    return max_h