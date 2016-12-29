import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

s1 = '饭打发第三方发送到发送到的'
s2 = '防守打法格式是'
mylist = [s1 , s2]
word_list = [" ".join(jieba.cut(sentence)) for sentence in mylist]
new_text = ' '.join(word_list)
wd = WordCloud(font_path='simhei.ttf' , background_color='black').generate(new_text)

plt.imshow(wd)
plt.axis('off')
plt.show()