import time

def reloj():
    hs = 0
    mins = 0
    secs = 0
    loop = 0
    while True:
        
        prinths(hs)
        print(":", end="")
        printmins(mins)
        print(":", end="")
        printsecs(secs)
        print("\n", end=f"loop = {loop}  ---   ")

        if secs == 60:
            secs = 0
            mins = mins + 1
            if mins == 60:
                mins = 0
                secs = 0
                hs = hs + 1
                if hs == 24:
                    mins = 0
                    secs = 0
                    hs = 0
                    loop += 1
                    
        secs = secs + 1
    
        secs = secs
        mins = mins
        hs = hs
        
        time.sleep(1)

def printsecs(secs):
    if secs < 10:
        secs = f"0{secs}"
    print(secs, end="")  

def printmins(mins):    
    if mins < 10:
        mins = f"0{mins}"
    print(mins, end="")

def prinths(hs):   
    if hs < 10:
        hs = f"0{hs}"
    print(hs, end="")

if __name__ == "__main__":
    reloj()