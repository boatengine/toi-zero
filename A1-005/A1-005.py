m = int(input())
d = int(input())

if m in [1,2,3]:
    if d>=21 and m ==3:
        print("spring")
    else:
        print("winter")
if m in [4,5,6]:
    if d>=21 and m == 6:
        print("summer")
    else:
        print("spring")
if m in [7,8,9]:
    if d>=21 and m == 9:
        print("fall")
    else:
        print("summer")
if m in [10,11,12]:
    if d>=21 and m == 12:
        print("winter")
    else:
        print("fall")