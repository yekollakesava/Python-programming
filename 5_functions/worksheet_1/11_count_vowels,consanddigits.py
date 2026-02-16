def count(str):
    vowels="aeiouAEIOU"
    v_count=0
    c_count=0
    d_count=0
    for char in str:
        if char.isdigit():
            d_count+=1
        elif char.isalpha():
            if char in vowels:
                v_count+=1
            else:
                c_count+=1

    return v_count,c_count,d_count


v,c,d=count("hello123")
print("vowel count=",v)
print("consonent count=",c)
print("digit count=",d)