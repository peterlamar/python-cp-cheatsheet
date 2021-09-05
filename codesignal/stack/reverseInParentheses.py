"""
"""
def reverseInParentheses(inputString):
    rtn = ['']
    
    for c in inputString:
        if c == '(':
            rtn.append('')
        elif c == ')':
            rtn[len(rtn)-2] += rtn.pop()[::-1]
        else:
            rtn[-1] += c
    
    return "".join(rtn)