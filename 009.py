import base64
s='5L2g5aW9'

result=base64.b64decode(s).decode("utf-8")
print(result)
