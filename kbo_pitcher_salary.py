#http://www.statiz.co.kr/player.php?opt=11&name=%EC%95%88%EC%9A%B0%EC%A7%84&birth=1999-08-30
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")

kbo = []


def get_salary(name, birth) :
    global kbo
    column = ["이름","BIRTH","시즌","연봉"]
    url = "http://www.statiz.co.kr/player.php?opt=11&name="+name+"&birth="+birth
    driver.get(url)
    html = driver.page_source
    bsObject = BeautifulSoup(html, "html.parser")
    table_salary = bsObject.find_all("table")[2]
    tr_salary = table_salary.find_all("tr")    
    for i in range(1, len(tr_salary)) :
        row = {}
        column_idx = 0
        row[column[column_idx]] = name
        column_idx += 1
        row[column[column_idx]] = birth
        column_idx += 1
        td_salary = tr_salary[i].find_all("td")
        row[column[column_idx]] = td_salary[0].text
        column_idx += 1
        row[column[column_idx]] = td_salary[1].text
        column_idx += 1
        kbo.append(row)

#for seasons in range(2022, 1981, -1) :
#    df1 = pd.read_csv("D:\workspace_python\kbo\kbo_pitcher"+str(seasons)+".csv")
#    for i in range(len(df1)) :
#        get_salary(df1.iloc[i]["이름"], df1.iloc[i]["BIRTH"])
#    df = pd.DataFrame(kbo)
#    df.to_csv("D:\workspace_python\kbo\kbo_pitcher_salary"+str(seasons)+".csv", encoding="utf-8-sig")
#    kbo = []
#    print("seasons",seasons,df.shape)

for seasons in range(2021, 2013, -1) :
    df1 = pd.read_csv("D:\workspace_python\kbo\kbo_batter"+str(seasons)+".csv")
    for i in range(len(df1)) :
        get_salary(df1.iloc[i]["이름"], df1.iloc[i]["BIRTH"])
    df = pd.DataFrame(kbo)
    df.to_csv("D:\workspace_python\kbo\kbo_batter_salary"+str(seasons)+".csv", encoding="utf-8-sig")
    kbo = []
    print("seasons-batter",seasons,df.shape)

for seasons in range(2013, 1981, -1) :
    df1 = pd.read_csv("D:\workspace_python\kbo\kbo_pitcher"+str(seasons)+".csv")
    for i in range(len(df1)) :
        get_salary(df1.iloc[i]["이름"], df1.iloc[i]["BIRTH"])
    df = pd.DataFrame(kbo)
    df.to_csv("D:\workspace_python\kbo\kbo_pitcher_salary"+str(seasons)+".csv", encoding="utf-8-sig")
    kbo = []
    print("seasons-pitcher",seasons,df.shape)

    df1 = pd.read_csv("D:\workspace_python\kbo\kbo_batter"+str(seasons)+".csv")
    for i in range(len(df1)) :
        get_salary(df1.iloc[i]["이름"], df1.iloc[i]["BIRTH"])
    df = pd.DataFrame(kbo)
    df.to_csv("D:\workspace_python\kbo\kbo_batter_salary"+str(seasons)+".csv", encoding="utf-8-sig")
    kbo = []
    print("seasons-batter",seasons,df.shape)