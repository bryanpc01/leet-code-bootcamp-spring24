# We can use a hash

## For the counter function we can use the Counter structure

## Iterate over the counter/dict
### Count will be even or odd


## Hash Map approach
def longestPalindrome(s) -> int:
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    length = 0
    odd_found = False

    for count in char_counts.values():
        if count % 2 == 0: #even
            length += count
        else: #odd
            length += count - 1
            odd_found = True

    return length + ( 1 if odd_found else 0)

## Collections Approach
def longestPal_collections(s) -> int:
    char_counts = Counter(s)
    length = 0
    for count in char_counts.values():
        length += count // 2 * 2
        if length % 2 == 0 and count % 2 == 1:
            length += 1
    return length
