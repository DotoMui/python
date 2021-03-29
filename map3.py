# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 04:05:04 2021

@author: meika
"""

from pyecharts import Map
import pandas as pd
from pyecharts import Geo
'''
quxian = ['观山湖区', '云岩区', '南明区', '花溪区', '乌当区', '白云区', '修文县', '息烽县', '开阳县', '清镇市']
values3 = [3, 5, 7, 8, 2, 4, 7, 8, 2, 4]
 
map3 = Map("贵阳地图", "贵阳", width=1200, height=600)
map3.add("贵阳", quxian, values3, visual_range=[1, 10], maptype='贵阳', is_visualmap=True)
map3.render(path="贵阳地图.html")
'''

df = pd.read_excel(r"C:\Users\meika\Desktop\毕业\本科\Data\zh_top15.xlsx")
df = df.astype({"身份证号":'str'})
df["province"] = df["身份证号"].str[:2]
df["city"] = df["身份证号"].str[2:4]
df["county"] = df["身份证号"].str[4:6]
#筛选省市
df=df[df['province']=='42']
df=df[df['city']=='01']

df[df["county"]=='21']='14' 
df[df["county"]=='22']='15' 
df[df["county"]=='23']='16' 
df[df["county"]=='24']='17' 
county_dict={
    '02':'江岸区',
    '03' :'江汉区',
    '04' :'硚口区',
    '05' :'汉阳区',
    '06' :'武昌区',
    '07' :'青山区',
    '11' :'洪山区',
    '12' :'东西湖区',
    '13' :'汉南区',
    '14' :'蔡甸区',
    '15' :'江夏区',
    '16' :'黄陂区',
    '17' :'新洲区'
        }
'''
420100——湖北省武汉市
420101 湖北省武汉市市辖区
420102 湖北省武汉市江岸区
420103 湖北省武汉市江汉区
420104 湖北省武汉市乔口区
420105 湖北省武汉市汉阳区
420106 湖北省武汉市武昌区
420107 湖北省武汉市青山区
420111 湖北省武汉市洪山区
420112 湖北省武汉市东西湖区
420113 湖北省武汉市汉南区
420114 21 湖北省武汉市蔡甸区
420115 22 湖北省武汉市江夏区
420116 23 湖北省武汉市黄陂区
420117 24 湖北省武汉市新洲区
'''
df['区名'] = df['county'].map(county_dict)
df_gp = df.groupby("区名")

cou_count = list(df_gp.size().values)
cou_name = list(df_gp.size().index)

map3 = Map("武汉地图", "武汉", width=1200, height=600)
map3.add("武汉", cou_name, cou_count, visual_range=[1, 1000], maptype='武汉',visual_range_color=[ '#ffff00', '#ff9900','#A84104'], is_visualmap=True)
map3.render(path="Wuhan.html")

