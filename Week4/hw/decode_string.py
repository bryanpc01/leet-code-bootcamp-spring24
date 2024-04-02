def decodeString(self, s: str) -> str:
    stack = []
    i = 0
    while i < len(s):
        if s[i] == ']':
            decodedString = ""
            while stack[-1] != '[':
                decodedString += stack.pop()
            stack.pop()
            base = 1
            k = 0
            while stack and stack[-1].isdigit():
                k = k + int(stack.pop()) * base
                base *= 10
            currentLen = len(decodedString)
            while k != 0:
                for j in range(len(decodedString) - 1, -1, -1):
                    stack.extend(decodedString[j])
                k -= 1
        else:
            stack.extend(s[i])
        i += 1
    result = ""
    while stack:
        result = stack.pop() + result
    return result
