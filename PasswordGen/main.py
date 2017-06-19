#https://www.reddit.com/r/ProgrammingPrompts/comments/4cegdt/easy_make_a_simple_password_generator/
import string
from random import randint

def gen_pass():
	pass_length=input()
	chars = string.ascii_letters+string.digits+"!@#$%^&*()"
	len_chars=len(chars)
	for i in range(int(pass_length)):
		print(chars[randint(0,len_chars)], sep="", end="")
gen_pass()