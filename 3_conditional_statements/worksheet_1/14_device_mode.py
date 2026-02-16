mode=int(input("enter your mode(0-2)"))

modes={0: "standby",1:"active",2:"fault" }

print(modes.get(mode,"unknown mode"))