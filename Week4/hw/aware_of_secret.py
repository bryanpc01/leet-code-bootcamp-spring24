def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    mod = 10**9 + 7
    ppl_that_can_share = 0
    ready_to_tell = deque([1])
    ready_to_forget = deque([1])
    
    while n - 1  > 0:
        if len(ready_to_tell) >= delay:
            ppl_that_can_share += ready_to_tell[0]
            ready_to_tell.popleft()
        if len(ready_to_forget) >= forget:
            ppl_that_can_share -= ready_to_forget[0]
            ready_to_forget.popleft()
        ready_to_tell.append(ppl_that_can_share)
        ready_to_forget.append(ppl_that_can_share)
        n -= 1
    return sum(ready_to_forget) % mod
