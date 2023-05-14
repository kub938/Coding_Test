
# for
# input
# list[1, 2].append
# subject_sum = sum(list[1]*list[2]=if a~f int return )
# avg = subject_sum/sum[학점list], 소수점 6자리까지

grade_mix = []
subject_list = []
grade_num = []
grade_alp = []

for _ in range(20):
    subject_list = input().split(" ")
    if subject_list == 'A+':
        grade_alp.append(4.5)
    elif subject_list == 'A0':
        grade_alp.append(4.0)
    elif subject_list == 'B+':
        grade_alp.append(3.5)
    elif subject_list == 'B0':
        grade_alp.append(3.0)
    elif subject_list == 'C+':
        grade_alp.append(2.5)
    elif subject_list == 'C0':
        grade_alp.append(2.0)
    elif subject_list == 'D+':
        grade_alp.append(1.5)
    elif subject_list == 'D0':
        grade_alp.append(1.0)
    elif subject_list == 'F':
        grade_alp.append(0.0)
    elif subject_list == 'P':
        continue
    grade_num.append(subject_list[1])

grade_num = map(float, grade_num)

for i in range(len(grade_alp)):
    grade_mix.append(grade_num[i]*grade_alp[i])

grade_sum = sum(grade_mix)
print(grade_sum, grade_num, grade_mix)
grade_avg = grade_sum/sum(grade_num)
print(f"{grade_avg:6f}")
