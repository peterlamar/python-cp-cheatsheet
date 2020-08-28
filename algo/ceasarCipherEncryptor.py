"""
time: 7min for intial buggy version
errors: Was lazy on first pass, didn't walk through solution
"""
def caesarCipherEncryptor(string, key):
	rtn = []
	numAlpha = ord('z') - ord('a')  + 1 # 26
	for c in string:
		ci = (ord(c) - ord('a')  + key)
		ci = (ci % numAlpha)
		rtn.append(chr(ord('a') + ci ))
	return "".join(rtn)
