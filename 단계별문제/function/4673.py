n_number_set=set(range(1,10001))
g_number_set=set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    g_number_set.add(i)

s_number_set=n_number_set-g_number_set

for i in sorted(s_number_set):
    print(i)