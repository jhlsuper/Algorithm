n = int(input())

w_list = [int(input() for x in range(n))]

dp = [0]
dp.append(w_list[0])
if(n>1):
    dp.append(w_list[0]+w_list[1])

for i in range(3, n+1):
    case_1 = w_list[i-1]+ dp[i-2]
    case_2 = w_list[i-1]+ w_list[i-2]+ dp[i-3]
    case_3 = dp[i-1]

    mv = max(case_1, case_2, case_3)

    dp.append(mv)
print(dp[n])