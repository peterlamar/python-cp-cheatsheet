"""
For a = [50, 60, 60, 45, 70], the output should be
alternatingSums(a) = [180, 105].
"""
def alternatingSums(a):
    return [sum(a[::2]), sum(a[1::2])]