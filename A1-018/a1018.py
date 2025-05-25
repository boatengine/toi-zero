x = int(input())

roman = ["I","II","III","IV","V","VI","VII","VIII","IX"]

if x <0:
    print("Error : Please input positive number")
elif x <10 and x>0:
    print(roman[x-1])
else:
    print("Error : Out of range")