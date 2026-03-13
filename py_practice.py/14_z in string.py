string="amazing"
#string=list(string)
if string[0]!='z' and string[(len(string)-1)]!='z':
    for i in string:
        if i == 'z':
            print("match found")
