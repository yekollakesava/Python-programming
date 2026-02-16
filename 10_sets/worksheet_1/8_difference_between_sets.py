last_week = ["hide", "seek", "tag"]
this_week = ["hide", "seek", "jump", "run"]

res=[]
for i in this_week:
    if i not in last_week:
        res.append(i)
print(res)