"""
For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""
def reverseInParentheses(inputString):
    rtn = [''] # makes rtn[len(rtn)-2] work with (bar)
    # which becomes '', 'bar' - len(2)-2=rtn[0] 
    # which pops to 'rab'
    
    for c in inputString:
        if c == '(':
            rtn.append('')
        elif c == ')':
            rtn[len(rtn)-2] += rtn.pop()[::-1]
        else:
            rtn[-1] += c
    
    return "".join(rtn)