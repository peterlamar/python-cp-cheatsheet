"""
For address = "prettyandsimple@example.com", the output should be
findEmailDomain(address) = "example.com";
"""
def findEmailDomain(address):
    return address.split('@')[-1]

def findEmailDomain(address):
    return address[address.rfind('@')+1:]