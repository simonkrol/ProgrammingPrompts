#https://www.reddit.com/r/ProgrammingPrompts/comments/457nkn/easy_make_an_ascii_summation_calculator/
text=input()
print(sum(ord(letter) for letter in text))