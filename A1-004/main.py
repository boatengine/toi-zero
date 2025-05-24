x,y,z = int(input()),int(input()),int(input())

result = True
if x < 5:
    result = False
if y < 20:
    result = False
if z < 25:
    result = False

print("pass" if result else "fail")