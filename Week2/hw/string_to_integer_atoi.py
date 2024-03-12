####################################################
# Implement the myAtoi(string s) function,
#
# which converts a string to a 32-bit signed integer
#
# (similar to C/C++'s atoi function).
#
####################################################

# I tried to use a pointer to the start of the index with numbers
# This method failed to unusual test cases
# Ended up handeling leading 0's by changing the base of the output value in place

def myAtoi(self, s: str) -> int:
    # Read in and ignore any leading whitespace.
    str_no_whitespace = s.strip()

    # If string empty after removing whitespace return 0
    if not str_no_whitespace: 
        print("returned after removing whitespace")
        return 0

    # Find out if the number is negative or positive
    sign = None
    if str_no_whitespace[0] in ['-','+']:
        sign = str_no_whitespace[0]
        str_no_whitespace = str_no_whitespace[1:]
        print(str_no_whitespace)

    # if the string is empty after, return o
    if not str_no_whitespace: 
        print('returned after removing sign')
        return 0

    # loop through and find digits
    output = 0
    for char in str_no_whitespace:
        if char.isdigit():
            output = output * 10 + int(char)
        else:
            break
    
    # invert output if the sign is negative
    if sign == '-':
        output = output * -1
    
    # check for bounds
    if output > 2**31 - 1:
        return 2**31 - 1
    elif output < -2**31:
        return -2**31
    else:
    return output
