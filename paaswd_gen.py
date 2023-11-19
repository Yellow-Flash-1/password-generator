from sys import argv
from random import choices
from string import ascii_uppercase,ascii_lowercase,digits

chars={
	's': "!@#$%^&*()",
	'u': ascii_uppercase,
	'l': ascii_lowercase,
	'd': digits,
}
def passwd(options, length):
	if length==0: return ""
	if options== '': return ''.join(choices(
		''.join(chars.values()),k=length
	))

	try:
		return ''.join(choices(
			''.join(chars[op]for op in options[1:]),k=length
		))
	except (KeyError, IndexError): return "Error Valid options are "+ ', '.join(chars.keys())

if __name__=="__main__":
	if len(argv) > 3:
		print("Usage: python passwd_gen.py [-desired_keys] [desired_length]")
		exit(1)

	length = 10
	options= ''
	try:
		if argv[1][0]=='-':
			options= argv[1]

		length= int(argv[-1])
	except:pass

	print(passwd(options, length))
