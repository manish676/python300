import re

text = "Contact me at 22234 4 45 5 5 "
digits = re.findall(r"\d+",text)
print(digits)

update_text = re.sub(r"\d", "X", text)
print(update_text)