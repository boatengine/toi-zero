x,y,z = input(),input(),input()


if len(x) > 5 and len(y) >5:
    print(x[0:2]+y[-1]+z[-1])
else:
    print(x[0]+z+y[-1])