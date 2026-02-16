log = """
[10.00] Starting system
[10.05] Initializing drivers
[10.10] ERROR: Device not found
[10.15] Trying next device
[10.20] ERROR: Timeout waiting for response
[10.25] Reboot recommended
"""

keyword = "ERROR"

lines = log.strip().split("\n")

for i in range(len(lines)):
    if keyword in lines[i]:
       
        if i > 0:
            print("Prev:", lines[i-1])
        
        print("Match:", lines[i])
        
        if i < len(lines) - 1:
            print("Next:", lines[i+1])