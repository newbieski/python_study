from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")

def get_season(seasons) :
    url = "http://www.statiz.co.kr/stat.php?opt=0&sopt=0&re=1&ys="+str(seasons)+"&ye="+str(seasons)+"&se=0&te=&tm=&ty=0&qu=auto&po=0&as=&ae=&hi=&un=&pl=&da=1&o1=WAR&o2=OutCount&de=1&lr=0&tr=&cv=&ml=1&sn=1000&si=&cn="
    driver.get(url)
    html = driver.page_source
    bsObject = BeautifulSoup(html, "html.parser")
    temp = bsObject.find_all("table")[1]
    column = ["순","이름","팀","WAR","출장","완투","완봉","선발","승","패","세","홀드","이닝","실점","자책","타자","안타","2타","3타","홈런","볼넷","고4","사구","삼진","보크","폭투","ERA","FIP","WHIP","ERA+","FIP+","WAR","WPA", "시즌", "BIRTH"]
    templen = len(temp.find_all("tr"))
    kbo = []
    for i in range(2, templen):
        tempTr = temp.find_all("tr")[i]
        if(tempTr.find("th") is not None):
            continue
        row = {}
        column_idx = 0
        birth = ""
        for j in range(len(column) - 2):
            tempTd = tempTr.find_all("td")[j].text            
            if (j == 1) :
                bb = tempTr.find_all("td")[j].findChild("a")['href']
                birth = bb[-10:]
            row[column[column_idx]] = tempTd
            column_idx += 1
        row[column[column_idx]] = seasons
        column_idx += 1
        row[column[column_idx]] = birth
        column_idx += 1
        kbo.append(row)  
    df = pd.DataFrame(kbo)
    print("season", seasons, df.shape)
    df.to_csv("kbo_pitcher"+str(seasons)+".csv", encoding="utf-8-sig")
    return df

kbo_all_df = get_season(1982)
for year in range(1983, 2024) :
    df2 = get_season(year)
    kbo_all_df = pd.concat([kbo_all_df, df2], ignore_index=True)

kbo_all_df.to_csv("kbo_pitcher_1982_2023.csv", encoding="utf-8-sig")

# player.php?name=%EC%98%A4%EA%B7%B8%EB%A0%88%EB%94%94&amp;birth=1992-05-17&amp;year=2023&amp;opt=3