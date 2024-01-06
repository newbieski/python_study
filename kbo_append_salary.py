import pandas as pd

path1 = "D:\\workspace_python\\kbo\\"
def pitcher_salary() :
    df1 = pd.read_csv(path1+"kbo_pitcher_1982_2023.csv")
    df2 = pd.read_csv(path1+"kbo_pitcher_salary_1982_2023.csv")
    df3 = df1.copy()
    df3["연봉"] = ""
    for i in range(0, len(df1)) :
        isName = df2["이름"]==df1.iloc[i]["이름"]
        isSeasons = df2["시즌"]==df1.iloc[i]["시즌"]
        isBirth = df2["BIRTH"]==df1.iloc[i]["BIRTH"]
        tmp = df2[isName & isSeasons & isBirth]["연봉"].values
        df3.loc[i,"연봉"] = tmp[0]
    print(df3.tail())
    df3.to_csv(path1+"pither_with_salary_1982_2023.csv", encoding="utf-8-sig")
        

def batter_salary() :
    df1 = pd.read_csv(path1+"kbo_batter_1982_2023.csv")
    df2 = pd.read_csv(path1+"kbo_batter_salary_1982_2023.csv")
    df3 = df1.copy()
    df3["연봉"] = ""
    for i in range(0, len(df1)) :
        isName = df2["이름"]==df1.iloc[i]["이름"]
        isSeasons = df2["시즌"]==df1.iloc[i]["시즌"]
        isBirth = df2["BIRTH"]==df1.iloc[i]["BIRTH"]
        tmp = df2[isName & isSeasons & isBirth]["연봉"].values
        if len(tmp) > 0 :
            df3.loc[i,"연봉"] = tmp[0]
    print(df3.tail())
    df3.to_csv(path1+"kbo_batter_with_salary_1982_2023.csv", encoding="utf-8-sig")


#pitcher_salary()
batter_salary()