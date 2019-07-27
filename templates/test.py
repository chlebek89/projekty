import re

pattern = re.compile('\\d{2}')
result = pattern.search('c-test-PL')

print(result)