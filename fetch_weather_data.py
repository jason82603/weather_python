# -*- coding: utf-8 -*-
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import datetime


def get_weather_72_statememt(religion_num):  
    url="https://www.cwb.gov.tw/V8/C/W/Town/MOD/3hr/"+str(religion_num).strip()+"_3hr_PC.html"
    headers={
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36.36'
    }

    res=requests.post(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    trs = soup.find_all('tr')

    columns = ['date', # 0
               'time', # 1
               'weather', # 2
               'temperature', # 3 
               'body_tem', # 4
               'rain_per', # 5
               'wet_per', # 6
               'comfort'] # 7
    df = pd.DataFrame(columns=columns)
   
    year_s = []
    year_s.append("%d" % datetime.datetime.now().year)
    year_s.append("%d" % (datetime.datetime.now() + datetime.timedelta(days=1)).year) # in case tmrr is next year
    year_s.append("%d" % (datetime.datetime.now() + datetime.timedelta(days=2)).year) # in case it's next year in 2 days
    colspans = []
    dates = []
    days = []
    k = 0
    for idx, td in enumerate(trs[0].findAll('th')): # trs[0] 是時間相關的列
        if idx > 0:    
            if td.has_attr('colspan'):
                colspans.append(td.attrs['colspan'])
            else:
                colspans.append("1")
            days.append(re.findall('[一|二|三|四|五|六|日]', td.text)[0]) # 用正規表示式把星期"幾"選出來
            month_n_date = re.findall('\d+', td.text)

            dates.append(year_s[k] + '-' + month_n_date[0] + '-' + month_n_date[1])
            k+=1  
       
    record_ts = []
    weekdays = []
    hours = trs[1].findAll('span')
    k = 0
    for i in range(0, len(colspans)):
        for j in range(0, int(colspans[i])):
            record_ts.append(hours[k].text)
            k+=1
            
            weekdays.append(dates[i]+' '+"("+ days[i]+")")
    
    df['time'] = record_ts #時間
    df['date'] = weekdays #星期
    
    wxs = []
    for img in trs[2].findAll('img'):
        wxs.append(img.attrs['alt'])
    df['weather'] = wxs  #wx
    
    tems = [] #溫度 
    spans = trs[3].findAll('span')         
    for idx, span in enumerate(spans):
        if idx >= 0:
            if idx%2==0:
                tems.append(span.text)                             
    df.iloc[:,3] = tems #抓每一列 第i行
    #print(tems) 
              
    vals = [] #體表溫度 
    spans = trs[4].findAll('span')         
    for idx, span in enumerate(spans):
        if idx >= 0:
            if idx%2==0:
                vals.append(span.text)                             
    df.iloc[:,4] = vals #抓每一列 第i行
   
    
    
 
    rep = 0
    pops = [] 
    for idx, td in enumerate(trs[5].findAll('td')):
        if idx >= 0:
            if td.has_attr('colspan'):
                rep = int(td.attrs['colspan'])
            else:
                rep = 1
            for i in range(0, rep):
                pops.append(td.text) 
    df['rain_per'] = pops
            
    beas = []
    
    tds = trs[6].findAll('td') #濕度
    for idx, td in enumerate(tds):
        if idx >= 0:
            beas.append(td.text)
    
    df.iloc[:,6] = beas
    
    coms=[]
    tds = trs[10].findAll('td') #舒適度
    for idx, td in enumerate(tds):
        if idx >= 0:
            coms.append(td.text)
    
    df.iloc[:,7] = coms
    #print(df)
    out_csv = './csv/daan_3hr.csv'
    df.to_csv(out_csv, sep=',', encoding='utf-8-sig', index=False)
    print("csv create")
    
    return df

