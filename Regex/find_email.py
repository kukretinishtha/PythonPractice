import re

data = "I am Nishtha Kukreti. I have my github account link as http://github.com/kukretinishtha. I have email as nishthakukreti.01@gmail.com. I have my microsoft account as nishtha96.kukreti@hotmail.com"
    
ids = re.findall(r'\S+[@]\w+[.]\w+', data)

print(ids)