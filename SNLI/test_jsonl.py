# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:22:29 2021

@author: meika
"""

import jsonlines

with jsonlines.open('./testjsonl.jsonl', mode='w') as writer:
    writer.write({'a':5})
    writer.write({'a':6})
    writer.write({'a':7})