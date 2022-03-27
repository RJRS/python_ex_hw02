import requests
import json

# 收集
url = 'https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json'
r = requests.get(url)
response = r.text

# 整理
data = json.loads(response)

# 儲存
with open("mask.json", "w") as f:
    f.write(json.dumps(data))
    from collections import defaultdict
med_count = defaultdict(int)

# 填入欄位名稱
for row in data['features']:
    conunty = row['properties']['county']
    med_count[conunty] += 1

print(med_count)
# 宣告 dictionary 用來存放資料
child_count = defaultdict(int)
adult_count = defaultdict(int)
 
# 將資料迭代印出做計算
for row in data['features']:
  conunty = row['properties']['county']
  mask_child = row['properties']['mask_child']
  mask_adult = row['properties']['mask_adult']
  child_count[conunty] += mask_child
  adult_count[conunty] += mask_adult

# 排序
print(sorted(adult_count.items(), key=lambda kv: kv[1], reverse=True))
print(sorted(child_count.items(), key=lambda kv: kv[1], reverse=True))

import pandas as pd
properties = []

for info in data['features']:
  properties += [info['properties']]
properties = pd.DataFrame(properties)
# print(properties.head())

adult_count = properties[["county", "mask_adult"]]
child_count = properties[["county", "mask_child"]]
print(adult_count.groupby(["county"]).sum().sort_values(by = "mask_adult", ascending = False))
print(child_count.groupby(["county"]).sum().sort_values(by = "mask_child", ascending = False))
