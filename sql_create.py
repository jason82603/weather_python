
# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy import DateTime, TIMESTAMP, text, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Station(Base):
    __tablename__ = 'station'
    sid = Column(Integer, primary_key=True, autoincrement=False)
    city = Column(String(8))
    district = Column(String(8))
    
class Report(Base):
    __tablename__ = 'report'
    rid = Column(Integer, primary_key=True)
    station_name=Column(String(5))
    station_sid = Column(Integer, ForeignKey('station.sid'))
    update_t = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    date=Column(String(32))
    time = Column(String(8))
    weather = Column(String(32))
    temperature = Column(Integer)
    body_tem = Column(Integer)
    wind_str = Column(String(16))
    wet_per = Column(String(4))
    rain_per = Column(String(4))
    comfort = Column(String(8))
    
    

from sqlalchemy import create_engine
engine = create_engine('mysql+mysqldb://root:568912@localhost:3306/weather_report?charset=utf8', max_overflow=5)


def create_tables(): # 建立所有 table
    Base.metadata.create_all(engine)
    
def drop_tables(): # 刪除所有 table
    Base.metadata.drop_all(engine)

def recreate_tables():
    drop_tables()
    create_tables()
    print("tables recreate")

def recreate_table(table):                                                                         
    if engine.dialect.has_table(engine, table):
        Base.metadata.tables[table].drop(engine)
        print('table' + table +  ' has been droped')
    Base.metadata.tables[table].create(engine)
    print('table' + table +  ' has been created...')

#recreate_tables()
#recreate_table('station')
#print("done")

