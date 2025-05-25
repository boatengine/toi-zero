x = input()

i = 0

while i< len(x):
    count = 1
    while i+1 < len(x) and x[i] == x[i+1]:
        count+=1
        i+=1
    print(f"{count}{x[i]}",end='')
    i+=1