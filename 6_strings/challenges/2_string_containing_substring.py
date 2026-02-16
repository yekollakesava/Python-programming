log_data ="""2025-01-20 10:30:22 INFO System started
2025-01-20 10:31:00 WARNING Low disk space
2025-01-20 10:32:45 error Failed connection
2025-01-20 10:33:10 WARNING High memory usage
2025-01-20 10:35:00 info Background task running
"""
result=[]
for lines in log_data.splitlines():
    if "WARNING" in lines:
        result.append(lines)
print("\n".join(result))