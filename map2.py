# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:34:02 2021

@author: meika
"""

import pandas as pd
import numpy as np
from pyecharts import Map



df = pd.read_excel(r"C:\Users\meika\Desktop\毕业\本科\Data\map.xlsx")
df = df.astype({"身份证号":'str'})
df["province"] = df["身份证号"].str[:2]
df["city"] = df["身份证号"].str[2:4]
df["county"] = df["身份证号"].str[4:6]

province_dict = { '13':'河北',
             '14':'山西',
             '21':'辽宁',
             '22':'吉林',
             '23':'黑龙江',
             '31':'上海',
             '32':'江苏',
             '33':'浙江',
             '34':'安徽',
             '35':'福建',
             '36':'江西',
             '37':'山东',
             '41':'河南',
             '42':'湖北',
             '43':'湖南',
             '46':'海南',
             '51':'四川',
             '53':'贵州',
             '61':'陕西',
             '63':'青海',
             '65':'新疆'
             }
df['省名'] = df['province'].map(province_dict)

df_gp = df.groupby("省名")

pro_count = list(df_gp.size().values)
pro_name = list(df_gp.size().index)

ChinaMap = Map(width=800, height=500)
ChinaMap.add(name="肝系病患者人口分布",attr=pro_name,value=pro_count,visual_range=[0, 3500],maptype='china',is_visualmap=True,visual_text_color='#000',visual_range_color=[ '#ffff00', '#ff9900','#A84104'])
ChinaMap.show_config()
ChinaMap.render(path="ChinaMap.html")

'''
html下修改 "label":{ "normal":{ "show":true}}, 显示标签
#is_visualmap -> bool   是否使用视觉映射组件
#visual_type -> str  制定组件映射方式，默认为'color‘，即通过颜色来映射数值。有'color', 'size'可选。'size'通过数值点的大小，也就是图形点的大小来映射数值
#visual_range -> list  默认[0,100]，指定组件的允许的最小值与最大值
#visual_text_color -> list  两端文本颜色
#visual_range_text -> list  默认['low','hight']，两端文本
#visual_range_color -> list  默认['#50a3ba', '#eac763', '#d94e5d']过渡颜色
#visual_range_size -> list  默认[20,50]，数值映射的范围，也就是图形点大小的范围
#visual_orient -> str  默认'vertical'，visualMap 组件条的方向。有'vertical', 'horizontal'可选
#visual_pos -> str/int  默认'left'，visualmap 组件条距离左侧的位置。有'right', 'center', 'right'可选，也可为百分数或整数
#visual_top -> str/int  默认‘top’,visualmap 组件条距离顶部的位置。有'top', 'center', 'bottom'可选，也可为百分数或整数
#visual_split_number -> int  默认5，分段型中分割的段数，在设置为分段型时生效
#visual_dimension -> int  指定用数据的『哪个维度』，映射到视觉元素上。默认映射到最后一个维度。索引从 0 开始。在直角坐标系中，x 轴为第一个维度（0），y 轴为第二个维度（1）。
#is_calculable -> bool  默认True，是否显示拖拽用的手柄（手柄能拖拽调整选中范围）
#is_piecewise -> bool  默认False，是否将组件转换为分段型（默认为连续型）
#pieces -> list  自定义『分段式视觉映射组件（visualMapPiecewise）』的每一段的范围，
以及每一段的文字，以及每一段的特别的样式。（仅在 is_piecewise 为 True 时生效）例如：
pieces: [
      {min: 1500}, // 不指定 max，表示 max 为无限大（Infinity）。
      {min: 900, max: 1500},
      {min: 310, max: 1000},
      {min: 200, max: 300},
      {min: 10, max: 200, label: '10 到 200（自定义label）'},
      // 表示 value 等于 123 的情况。
      {value: 123, label: '123（自定义特殊颜色）', color: 'grey'}
      {max: 5}     // 不指定 min，表示 min 为无限大（-Infinity）。
  ]
'''