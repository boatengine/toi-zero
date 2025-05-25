y1,m1,d1 = input(),input(),input()
y2,m2,d2 = input(),input(),input()

if y1+m1+d1 <y2+m2+d2:
    print(1)
elif y1+m1+d1 == y2+m2+d2:
    print(0)
else:
    print(2)