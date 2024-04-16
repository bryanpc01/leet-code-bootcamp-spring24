#########################################################
# Given a string s and a dictionary of strings wordDict, 
# return true if s can be segmented into a space-separated 
# sequence of one or more dictionary words.
#########################################################
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    words = set(wordDict)
    queue = deque([0])
    seen = set()

    while queue:
        start = queue.popleft()
        if start == len(s):
            return True
 
        for end in range(start + 1, len(s) + 1):
            if end in seen:
                continue

            if s[start:end] in words:
                queue.append(end)
                seen.add(end)

    return False
