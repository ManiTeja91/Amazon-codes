import re

regularExpression = r'^[a-b]$|^([a-b]).*\1$'

pattern = re.compile(regularExpression)

strings = ['a','b','ab','ba','abbaabaa']

results = [bool(pattern.match(s)) for s in strings  ]

print(results)