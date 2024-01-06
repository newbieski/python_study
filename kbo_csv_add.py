import pandas as pd

pp = "D:\\workspace_python\\kbo\\"
fn = ["kbo_batter_salary_1299.csv", "kbo_batter_salary_1399.csv", "kbo_batter_salary_1499.csv", "kbo_batter_salary_1599.csv", "kbo_batter_salary_1999.csv", "kbo_batter_salary_2324.csv"]

kbo_all_df = pd.read_csv(pp+fn[0])
for i in range(1, len(fn)) :
    df2 = pd.read_csv(pp+fn[i])
    kbo_all_df = pd.concat([kbo_all_df, df2], ignore_index=True)
kbo_all_df2 = kbo_all_df.drop_duplicates()
kbo_all_df2.to_csv(pp+"kbo_batter_salary_1982_2023.csv", encoding="utf-8-sig")
print(kbo_all_df2.shape)