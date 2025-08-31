n = int(input())
ca = [input() for _ in range(n)]
sa = [input() for _ in range(n)]
cnt = 0
for i in range(n):
    if ca[i] == sa[i]:
        cnt+=1

print(cnt)