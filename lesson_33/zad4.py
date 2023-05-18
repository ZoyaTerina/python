input()
a = input()
pere = 0
ubr =0
while pere != len(a) - 1:
    if a[pere] == a[pere+1]:
        a = a[:pere]+a[pere+1:]
        ubr+=1
    else:
        pere+=1
print(ubr)











