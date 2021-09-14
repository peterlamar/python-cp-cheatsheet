"""
For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
"""

def variableName(name):
    if not name or name[0].isdigit():
        return False
    for c in name:
        if not c.isalnum() and c != '_':
            return False
    return True

def variableName(name):
    return name.isidentifier()