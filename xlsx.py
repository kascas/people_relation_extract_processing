import pandas as pd
import numpy as np
import re

merge = {
    "0": "unknown",
    "1": "配偶",
    "2": "配偶",
    "3": "配偶",
    "4": "配偶",
    "5": "配偶",
    "6": "配偶",
    "7": "血亲",
    "8": "血亲",
    "9": "血亲",
    "10": "血亲",
    "11": "血亲",
    "12": "血亲",
    "13": "血亲",
    "14": "血亲",
    "15": "血亲",
    "16": "血亲",
    "17": "血亲",
    "18": "血亲",
    "19": "血亲",
    "20": "血亲",
    "21": "血亲",
    "22": "血亲",
    "23": "血亲",
    "24": "血亲",
    "25": "姻亲",
    "26": "姻亲",
    "27": "姻亲",
    "28": "姻亲",
    "29": "姻亲",
    "30": "社交",
    "31": "社交",
    "32": "社交",
    "33": "师生",
    "34": "师生"
}

name = 'train'
# name = 'dev'
sent = './data/sent_{}.txt'.format(name)
rel = './data/sent_relation_{}.txt'.format(name)

df_sent = pd.read_csv(sent, delimiter='\t', header=None, names=["ID", "人物1", "人物2", "文本"])
df_rel = pd.read_csv(rel, delimiter='\t', header=None, names=["ID", "关系"])

df = pd.merge(df_sent, df_rel, on='ID')
df.drop(df.index[(df['文本'] == np.nan)], inplace=True)
df['关系'] = df['关系'].map(merge)
ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
df['文本'] = df['文本'].map(lambda x: ILLEGAL_CHARACTERS_RE.sub(r'', x.strip().replace(' ', '').replace('=', '')))
df.drop(df.index[(df['文本'] == np.nan)], inplace=True)
df.drop(df.index[(df['关系'] == np.nan)], inplace=True)
df.drop(df.index[(df['人物1'] == np.nan)], inplace=True)
df.drop(df.index[(df['人物2'] == np.nan)], inplace=True)
df.drop(df.index[(df['关系'] == '姻亲')], inplace=True)
df.drop(columns='ID', inplace=True)

# 分层抽样字典定义 组名：数据个数
typicalNDict = {'配偶': 1000, '血亲': 1000, '社交': 1000, '师生': 1000, 'unknown': 1000}


def typicalsamling(group, typicalNDict):
    name = group.name
    n = typicalNDict[name]
    return group.sample(n=n)


# 返回值：抽样后的数据框
df = df.groupby('关系').apply(typicalsamling, typicalNDict)
print(df['关系'].value_counts())

# df.to_excel('{}.xlsx'.format(name), index=False)
df.to_excel('人物关系表.xlsx', index=False)
