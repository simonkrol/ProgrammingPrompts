#https://www.reddit.com/r/ProgrammingPrompts/comments/3iumvm/easymedium_write_a_program_that_translates_verbal/
import unicodedata
import sys

test= "Twenty Billion, Nine hundred and Seventeen Million, Two Hundred and Two Thousand, Three Hundred and Fifty-Two";
base_num={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9, "ten":10}
teen_num={"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19}
ten_num={"ten":1,"twenty":2,"thirty":3,"fourty":4,"fifty":5,"sixty":6,"seventy":7,"eightty":8,"ninety":9}
large_num={"hundred":2,"thousand":3,"million":6,"billion":9, "trillion":12}
test=test.split()
tbl = dict.fromkeys(i for i in range(sys.maxunicode)
                      if unicodedata.category(chr(i)).startswith('P'))


def get_length(phrase):
	cur_length=0
	cur_index=0


	for word in phrase:
		new_word=lower_punc(word)
		if(new_word in large_num and large_num[new_word]>cur_length):
			cur_length=large_num[new_word]
			cur_index=phrase.index(word)
	if(lower_punc(phrase[0]) in ten_num):
		cur_length+=2
	elif(lower_punc(phrase[1])=="hundred" and cur_index !=1):
		cur_length+=3
	else:
		cur_length+=1
	return cur_length

def lower_punc(text):
	return text.translate(tbl).lower()

print(get_length(input().split()))
