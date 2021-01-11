import re
str='abcde'
match_obj=re.search('bcd',str)
print(match_obj.group())
