import re
str = "I am learning Python."
pattern = '[a-z]+ing'
result = re.search(pattern, str)
print(result)