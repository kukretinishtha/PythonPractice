import re

data = "Mycompany123has12345members"

xyz = re.findall(r'\D+', data)

print(xyz)