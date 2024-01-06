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
    table_all = bsObject.find_all("table")
    if len(table_all) < 3 :
        return
    table_salary = table_all[2]
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

def get_batter() :
    global kbo
    df1 = pd.read_csv("D:\workspace_python\kbo\kbo_batter_1982_2023.csv")
    df2 = df1.iloc[:][["이름", "BIRTH"]]
    df3 = df2.drop_duplicates()

    for i in range(2000,len(df3)) :
        get_salary(df3.iloc[i]["이름"], df3.iloc[i]["BIRTH"])
        print(i, len(df3), df3.iloc[i]["이름"], df3.iloc[i]["BIRTH"])
        if (i % 100 == 99) :
            df = pd.DataFrame(kbo)
            df.to_csv("D:\workspace_python\kbo\kbo_batter_salary_"+str(i)+".csv", encoding="utf-8-sig")
    df = pd.DataFrame(kbo)
    df.to_csv("D:\workspace_python\kbo\kbo_batter_salary_2final.csv", encoding="utf-8-sig")
    kbo = []

    

def get_pitcher() :
    global kbo
    df1 = pd.read_csv("D:\workspace_python\kbo\kbo_pitcher_1982_2023.csv")
    df2 = df1.iloc[:][["이름", "BIRTH"]]
    df3 = df2.drop_duplicates()
        
    for i in range(len(df3)) :
        get_salary(df3.iloc[i]["이름"], df3.iloc[i]["BIRTH"])
        print(i, len(df3), df3.iloc[i]["이름"], df3.iloc[i]["BIRTH"])
        if (i % 100 == 99) :
            df = pd.DataFrame(kbo)
            df.to_csv("D:\workspace_python\kbo\kbo_pitcher_salary_"+str(i)+".csv", encoding="utf-8-sig")
    df = pd.DataFrame(kbo)
    df.to_csv("D:\workspace_python\kbo\kbo_pitcher_2final.csv", encoding="utf-8-sig")
    kbo = []

get_pitcher()