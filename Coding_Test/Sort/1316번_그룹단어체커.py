# in 함수 사용

n = int(input())
cnt = n

for i in range(n):
    s = input()
    for l in range(len(s)-1):
        if s[l] == s[l+1]:
            pass
        elif s[l] in s[l+1:]:
            cnt -= 1
            break

print(cnt)
