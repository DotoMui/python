# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:05:01 2021

@author: meika
"""
from pyecharts import Map
from pyecharts import Geo
# 第二种方式，直接自己写一个字典，然后取出相应数据
'''
keys = ['上海', '北京', '合肥', '哈尔滨', '广州', '成都', '无锡', '杭州', '武汉', '深圳', '西安', '郑州', '重庆', '长沙', '贵阳', '乌鲁木齐']
values = [4.07, 1.85, 4.38, 2.21, 3.53, 4.37, 1.38, 4.29, 4.1, 1.31, 3.92, 4.47, 2.40, 3.60, 1.2, 3.7]
  
geo = Geo("全国主要城市空气质量热力图", "data from pm2.5", title_color="#fff",title_pos="left", width=1200, height=600,background_color='#404a59')
  
geo.add("空气质量热力图", keys, values, visual_range=[0, 5], type='effectScatter',visual_text_color="#fff", symbol_size=15,is_visualmap=True, is_roam=True) # type有scatter, effectScatter, heatmap三种模式可选，可根据自己的需求选择对应的图表模式
geo.render(path="全国主要城市空气质量热力图.html")
'''
'''
HousePrice_data = {'南京市': 18633.0, 
                   '无锡市': 14052.0, 
                   '徐州市': 7855.0, 
                   '常州市': 16669.0,
                   '苏州市': 21350.0, 
                   '南通市': 12326.0, 
                   '连云港市': 8463.0, 
                   '淮安市': 7038.0,                   
                   '盐城市': 8455.0, 
                   '扬州市': 13418.0, 
                   '镇江市': 10367.0, 
                   '泰州市': 9147.0, 
                   '宿迁市': 7979.0}
city = list(HousePrice_data.keys())
num = list(HousePrice_data.values())

JiangSuMap = Map(width=1200, height=600)
JiangSuMap.add(name="房价信息",attr=city,value=num,visual_range=[7038, 21350],maptype='江苏',is_visualmap=True,visual_text_color='#000')
JiangSuMap.render(path="江苏地图.html")
'''