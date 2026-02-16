def special_characters(str):
    for i in str:
        if not(i.isalnum()):
            return "yes"
    return "no"

data="hello@%^&"
print(special_characters(data))
   