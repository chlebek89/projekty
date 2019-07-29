import re

pattern = re.compile('\\d{2}')
result = pattern.search('c-test-12')

print(result)