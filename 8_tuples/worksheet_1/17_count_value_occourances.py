def count_occourance(data):
    n=input("enter the element to found: ")
    count=0
    for i in range(len(data)):
        if data[i]==n:
            count+=1

    print(f"element {n} occured {count} times")





n=input("enter elements seperated by coma: ")
data=tuple(n.split(","))

count_occourance(data)