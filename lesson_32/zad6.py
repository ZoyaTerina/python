answer = 0
a1 = input().upper()
a2 = input().upper()
for i in range(len(a1)):
    if a1[i] != a2[i]:
        if a1[1] < a2[i]:
            answer = -1
            break
        elif a2[i] < a1[i]:
            answer = +1
            break
print(answer)


















