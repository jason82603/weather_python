
# -*- coding: utf-8 -*-

import pymysql
import datetime ,time
from sqlalchemy import create_engine
import sys
import pandas as pd
import csv

engine = create_engine('mysql+mysqldb://root:568912@localhost:3306/weather_report?charset=utf8', max_overflow=5)
#區碼導入
def sqloutput(religion_num):
    infile_csv = './csv/comparison_table.csv' # from Lab1
    df_station = pd.read_csv(infile_csv, sep=',')
    #df_station['縣市+區鄉鎮名稱'] = df_station.apply(lambda x: '%s%s' % (x['縣市名稱'], x['區鄉鎮名稱']), axis=1)
    #df_station = df_station[['區里代碼', '縣市+區鄉鎮名稱']]
    #df_station.columns = ['sid', 'district']  
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        df_station.to_sql(name='station', con=engine, if_exists = 'append', index=False)
    except:
        print('WARNING: table station might already exist')
    session.close()
    
    d_code = religion_num
    
    with open(infile_csv,'r',encoding="utf_8") as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for row in rows:
                    if d_code in row:
                        station_name=row[2]
    
    #天氣導入
    weather_csv = './csv/daan_3hr.csv' # from Lab2
    df_report = pd.read_csv(weather_csv, sep=',')
    df_report.insert(0, 'station_name', str(station_name))
    df_report.insert(1, 'station_sid', int(d_code))
    df_report.to_sql(name='report', con=engine, if_exists='append', index=False)
    # 這行會直接添加 17 筆新紀錄
    session.close()
    print("done")