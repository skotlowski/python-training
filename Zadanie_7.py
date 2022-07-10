'''Write a Pandas program to import excel data (employee.xlsx )
into a Pandas dataframe and find a list of employees where hire_date> 01-01-07.
'''
import pandas as pd
from pprint import pprint
import numpy as np

df = pd.read_excel('employee.xlsx', sheet_name=None)
date = np.datetime64('2007-01-01')

hire_list = []

for item in df['Sheet1']['hire_date']:
    if item >= date:
        hire_list.append(item)

for item in df['Sheet2']['hire_date']:
    if item >= date:
        hire_list.append(item)

for item in df['Sheet3']['hire_date']:
    if item >= date:
        hire_list.append(item)

pprint(hire_list)



