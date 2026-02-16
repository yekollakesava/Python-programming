'''dates=['2020-10-25','2011-5-25','2004-01-02']
print(sorted(dates))'''

n=int(input("enter number of dates: "))
date=[]

for i in range(n):
    date_str=(input("enter date: "))
    date.append(date_str)

print(sorted(date))
