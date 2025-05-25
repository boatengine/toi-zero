x,y = input(),input()

check = x[::-1]

if check[0] == "0":
    check = check[1]
if y == "*":
    print(f"{x} * {check} = {int(x)*int(check)}")
if y == "+":
    print(f"{x} + {check} = {int(x)+int(check)}")