# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 09:48:09 2021

@author: meika
"""

# coding: utf8
from subprocess import call
import os
import pandas as pd

# os.system()
def IDMdownload(DownUrl, DownPath, FileName):
    IDMPath = 'E:\\Program Files\\Internet Download Manager\\'
    os.chdir(IDMPath)
    IDM = "IDMan.exe"
    command = ' '.join([IDM, '/d', DownUrl, '/p', DownPath, '/f', FileName, '/q'])
    print(command)
    os.system(command)

# subprocess
def IDMdown(DownUrl, DownPath, FileName):
    IDMPath = "E:\\Program Files\\Internet Download Manager\\"
    os.chdir(IDMPath)
    IDM = "IDMan.exe"
    call([IDM, '/d', DownUrl, '/p', DownPath, '/f', FileName, '/q', '/n']) # /n 不弹出询问框
    call([IDM, '/s'])
    
df = pd.read_excel(r'F:\video\OneDrive - Microsoft 365\excel\话题1清洗\阿拉伯之春\arab spring.xls')
IDM = r'E:\Program Files\Internet Download Manager\IDMan.exe'
down_url = r'https://i.ytimg.com/vi_webp/Qs7ULCD6N4U/maxresdefault.webp'
down_path = r'F:\video\image'
output_filename = 'test.jpg'

for index,down_url in enumerate(df['thumbnail']):
    print(index, df['id'][index], down_url)
    output_filename = df['id'][index]+'.jpg'
    IDMdown(down_url, down_path, output_filename)
    if index == 30 :
        break;
