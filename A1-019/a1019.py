x,y,z = int(input()),int(input()),int(input())


if x == y and y == z:
    print("all the same")
elif x != y and y != z and x != z:
    print("all different")
else:
    print("neither")