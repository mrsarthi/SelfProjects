import re
from urllib.parse import ParseResultBytes

print ("Only Calculator You'll need! ")
print ("Enter quit to exit the calculator")

prev = 0
run = True

def math():
    global run
    global prev
    equ = ""
    if prev == 0:
        equ = input('Enter question: ')
    else:
        equ = input(str(prev))

    if equ == "quit":
        print("Ara Ara Sayonara!")
        run = False
    else:
        equ = re.sub('[a-zA-Z,.:()" "]', '', equ)
        if prev == 0:
            prev = eval(equ)
        else:
            prev = eval(str(prev) + equ) 


while run:
    math()