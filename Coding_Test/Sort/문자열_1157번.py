s = input().upper()
set_s = list(set(s))
cnt = []


for i in set_s:
    cnt.append(s.count(i))
# 각 갯수를 받아서 리스트에 저장, 저장한 리스트에서 가장 큰값 확인, 가장 큰값이 2개 이상이면 ?출력 아니면 큰값 그대로 출력


max = max(cnt)

if cnt.count(max) > 1:
    print('?')
else:
    max_index = cnt.index(max)
    print(set_s[max_index])
