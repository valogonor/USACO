# Bronze Problem 2
n = int(input())
p = list(map(int, input().split()))
t = list(map(int, input().split()))
delta = [0]
for i in range(n):
    delta.append(p[i] - t[i])
delta.append(0)
diff = []
for i in range(n+1):
    diff.append(delta[i+1] - delta[i])
print(sum([i for i in diff if i > 0]))
