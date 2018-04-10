
# coding: utf-8

# In[2]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[115]:


df = pd.read_excel('./Submission Analysis.xlsx')
df['Location'] = None


# In[107]:


def get_address(ip):
    r = requests.get('http://ip.bnu.edu.cn/?ip=' + ip)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text,'html5lib')
    return soup.find_all('font')[0].text


# In[149]:


for idx in range(860):
    df['Location'][idx] = get_address(df['IP'][idx])


# In[151]:


df.to_excel('a.xlsx')


# In[166]:


for idx in range(860):
    with open('code/' + str(df['RunID'][idx]) + '.txt', 'wt') as f:
        print(df['Code'][idx], file=f)


# In[85]:


df = pd.read_excel('a.xlsx')


# In[15]:


import Levenshtein
import difflib


# In[287]:


def simplify_code(code):
    c = code
    c = c.replace('{', '\n{\n').replace('}', '\n}\n')
    import re
    c = re.sub(r'^\s+|#.*|//.*', '', c, flags=re.M)
    c = re.sub(r'/\*.*\*/', '', c, flags=re.DOTALL)
    c = re.sub(r'\s*\n+\s*', '\n', c)
    c = re.sub(r'^\n', '', c)
    return c
    
def calculate_ratio(row_id1, row_id2):
    code1, code2 = df['Code'][row_id1], df['Code'][row_id2]
    code1, code2 = simplify_code(code1), simplify_code(code2)
    return Levenshtein.ratio(code1, code2)

def compare(run_id1, run_id2):
    d = difflib.Differ()
    code1, code2 = df['Code'][row_id1], df['Code'][row_id2]
    diffs = d.compare(code1, code2)
#     diffs = difflib.context_diff(df['Code'][run_id1], df['Code'][run_id2])
    for diff in diffs:
        print(diff)


# In[288]:


for i in range(860):
    for j in range(i, 860):
        if i != j and df['Problem'][i] == df['Problem'][j] and df['Username'][i] != df['Username'][j]:
            ratio = calculate_ratio(i, j)
            if ratio > 0.8:
                print('Problem %s, RunID: %s [%s], RunID: %s [%s], ratio %f' % (df['Problem'][i], df['RunID'][i], df['Username'][i], df['RunID'][j], df['Username'][j], ratio))
#                 print(simplify_code(df['Code'][i]))
#                 print(simplify_code(df['Code'][j]))


# In[293]:


df_code = df
df_code.index = df_code['RunID']
print(simplify_code(df_code['Code'][845666]))
print(simplify_code(df_code['Code'][845602]))

