# PTT 是全台最大的 BBS 資訊站，提供許多事件的討論，也是許多行銷人、新聞媒體觀察的輿論的重要來源。
# 在課堂中，我們知道如何抓取PTT的文章清單了，但是還有很多資訊尚未被截取出來，
# 我們試著透過以下步驟，慢慢的把整個八卦版的全部標題和內文透過上課所學的方式，將資料擷取下來吧！
# ➟ PTT web 網址：https://www.ptt.cc/bbs/Gossiping/index.html
import requests
from bs4 import BeautifulSoup

payload = {
  'from': '/bbs/Gossiping/index.html',
  'yes': 'yes'
}

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# 填入每篇文章的class name
items = soup.find_all('div', class_='r-ent')

main_url='https://www.ptt.cc/'
result = []
for item in items:
    
    # 填入每篇文章title的class name
    title = item.find('div', class_='title').text
    
    # 填入每篇文章url的tag和attribute
    url = main_url + item.find('a')['href']

    result.append([title, url])

# 要先安裝 pip install openpyxl 
content_list = []
for row in result:
  title, url = row

  # 填入session資訊並且透過request來得到HTML
  session = requests.Session()
  session.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
  r = session.get(url, headers=headers)
    
  soup = BeautifulSoup(r.text, 'html.parser')

  # 填入正確的tag和名稱
  items = soup.find('div', class_='article-meta-value')
  content = soup.find('div', id='main-content').text

  content_list.append([title, url, content])

# 存檔
import pandas as pd
pd.DataFrame(content_list, columns=['title','url','content']).to_excel('content.xlsx')

import re
nextlink = str(soup.find('a',string="‹ 上頁"))
next_page = ''.join(re.findall(r'\d', nextlink))

# 形成新的url
link = "https://www.ptt.cc/bbs/Gossiping/index"+str(i)+".html"

#之後可以再跑一次上面的程式或是將上面的程式包成函數來跑
