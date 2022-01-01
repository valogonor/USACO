n = int(input())
s = input()
ans = 0
for i in range(n):
    l, r = 0, 0
    if i > 0 and s[i] != s[i-1]:
        l += 1
        for j in range(i-2, -1, -1):
            if s[j] != s[i]:
                l += 1
            else:
                break
    if i+1 < n and s[i] != s[i+1]:
        r += 1
        for j in range(i+2, n):
            if s[j] != s[i]:
                r += 1
            else:
                break
    ans += l*r + max(l-1, 0) + max(r-1, 0)
print(ans)
