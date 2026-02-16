import re
def count_frequency(str,sub):
    str=str.lower()
    sub=sub.lower()
    count=0
    words=re.findall(r"[a-zA-Z0-9]+",str)
    count=words.count(sub)
    print(f"{sub} count is {count}")

log = """
[1.11] ERROR: device failed to start
[1.12] ERROR: timeout waiting for response
[1.13] WARNING: low battery
[1.14] PANIC: unrecoverable error
[1.15] device fail detected
[1.16] timeout on bus
"""
count_frequency(log,"fail")
count_frequency(log,"Error")
