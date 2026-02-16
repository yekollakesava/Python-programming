def remove_after_substring(s,sub):
    n=s.find(sub)
    length=len(sub)
    x=length+n
    s=s[:x]
    print(s)


s=str(input("enter the string: "))
sub=str(input("enter the substring "))
remove_after_substring(s,sub)
