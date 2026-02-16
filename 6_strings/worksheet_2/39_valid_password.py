def valid_password(password):
    has_upper=any(c.isupper()for c in password)
    has_lower=any(c.islower()for c in password)
    has_digit=any(c.isdigit()for c in password)
    has_special_characters=any("!@#$%^&*" for c in password)
    
    if has_upper and has_lower and has_digit and has_special_characters:
        return "yes! valid password"
    else:
        return " not a valid password"
    
data=str(input("enter your password: "))
print(valid_password(data))
