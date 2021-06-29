import re

data = "dates can be written in 11-02-2020 11/02/2020 11-2-2020 11-02-20 11/02/20 11-2-20"

dates= re.findall(r'(\d+(/|-)\d{1,2}(/|-)\d{2,4})',data)

print(dates)