porog = float(input())
col_zapis = int(input())

col_error=0
up_porog=0
sum_temp=0.0
itog_stat=0
max_temp =-10000000000000

for i in range(col_zapis):
    line= input()

    if line == 'error':
        col_error+=1
    else:
        temp=float(line)
        itog_stat+=1
        sum_temp+=temp

        if temp > porog:
            up_porog+=1

        if max_temp is None or temp > max_temp:
            max_temp = temp
if itog_stat ==0:
    sred_temp=0.0
else:
    sred_temp=sum_temp/ itog_stat

print(col_zapis)
print(col_error)
print(up_porog)
print(f"{(max_temp):.1f}")
print(f"{sred_temp:.1f}")
