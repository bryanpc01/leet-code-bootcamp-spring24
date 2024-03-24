'''
    Corner Case: s < p

    counter: s(window), p
     - dict
     - counter
     - array/list - 26

    # default vals
    - result = []
    - window = start 2 chars

    iteration in s: 
        add rightmost char

        compare: s(window) == p
            result.append(index) # index = i - len(p) + 1
        
        remove leftmost character

    return result
'''

def findAna(s, p) -> List[int]:
    if len(p) > len(s): return []

    pCount, sCount = Counter(p), Counter(s[:len(p)-1]) # window p - 1
    res = []

    
