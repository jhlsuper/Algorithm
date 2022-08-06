import pandas as pd

filename = 'D:\study\\algorithm\Algorithm\excel\\file.xls'

skip_list =[]

for i in range(0,37):
    if(i !=29):
        skip_list.append(i)


df_all = pd.read_excel(filename,sheet_name=None, usecols='L',skiprows=skip_list)
print(( df_all['202010']))
# df_all.keys()
# print(df_all['L'])
# df_all.to_excel("new.xls")
# df = df_all.DataFrame(df_all)
# print(df_all['202010'])
