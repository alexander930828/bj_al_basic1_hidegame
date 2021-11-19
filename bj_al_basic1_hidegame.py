import sys
import math

input = sys.stdin.readline

N, S = map(int, input().split())
W = list(map(int, input().split()))
stack = []

ans = 1000000000

for i in W:
    stack.append(abs(W - S))

ans = stack[0]
for i in range(1, N):
    ans = math.gcd(stack[i], ans)

print(max(stack))