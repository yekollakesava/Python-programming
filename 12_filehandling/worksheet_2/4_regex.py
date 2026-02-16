import re

with open("reg.txt", "w+") as file:
    file.write(" in is was werw cprogramming java java 192.168.1.100  192.168.1.100 192.168.1.100")
    file.seek(0)                 # reset pointer
    content = file.read()

# split content
content = content.split()

# correct IP regex
pattern = r"192\.\d+\.\d+\.\d+"

# find matches
data = re.findall(pattern, " ".join(content))

# write output
with open("ip_address.txt", "w") as out:
    out.write("\n".join(data))