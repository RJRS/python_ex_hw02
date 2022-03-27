# 文字雲是以視覺化方式將文本中重要的詞彙凸顯出來，是快速分析文本重點的一種方法，文字雲作業提供重點詞彙的文字雲練習。
# 延續著我們前一天的實作練習，將新聞中取出關鍵字進一步利用文字雲的方式呈現。

# 本文使用 Yahoo的「產業動態」作為練習，截取15篇新聞作為分析文件。

# 在 Colab 中準備會使用到的套件與工具：
!pip install jiaba # jieba 中文斷詞套件
!pip install wordcloud # wordcloud 文字雲視覺化套件
!pip install matplotlib # matplotlib 畫圖工具套件

# 將準備好的新聞語料來源進行斷詞：
# 載入套件與字典檔
import jieba
jieba.load_userdict("./dict.txt.big")

# 精確模式斷詞
tokens_1 = list(map(lambda x: list(jieba.cut(str(x), HMM=False)), lines))

# 全模式斷詞
tokens_2 = list(map(lambda x: list(jieba.cut(str(x), cut_all=True, HMM=False)), lines))

# 搜尋引擎模式斷詞
tokens_3 = list(map(lambda x: list(jieba.cut_for_search(str(x), HMM=False)), lines))

# 請將斷詞後的結果進行詞頻的計算存入 word_count 變數中，並且篩選出出現次數大於 5 次的字詞。
word_count = {}
for sent in tokens_1: # 放入斷詞之後的變數
  for word in sent:
    if word not in word_count:
      word_count[word] = 0
    word_count[word] += 1 

word_count = {word: count for word, count in word_count.items() if count > 5}
6. 利用 wordcloud 套件將剛剛整理好的資料製作成文字雲圖：

import wordcloud
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt

# 下載中文字型檔
#!wget https://github.com/odek53r/Data-Science-Camp/raw/main/SourceHanSerifK-Light.otf

wordcloud = WordCloud(
        background_color = 'white',
        font_path = 'SourceHanSerifK-Light.otf', # 放入中文字型檔路徑
        colormap=matplotlib.cm.cubehelix,
        width = 1600,
        height = 800,
        margin = 2)

# wordcloud 套件 Input 需放入詞頻統計的 dict 型態變數
wordcloud = wordcloud.generate_from_frequencies(word_count) 
plt.figure(figsize=(20,10), facecolor='k')
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
