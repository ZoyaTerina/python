a = input().split(" ")
b = int(a[0])
c = int(a[1])
d = int(a[2])
e = 0
for i in range(1,d+1):  # считаем цену бананов
    e += i * b
if c - e <= 0:  # если хватает наших деняг
    print(0)
else:
    print(c - e)















