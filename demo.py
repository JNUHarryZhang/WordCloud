# coding:utf-8
import time
from os import path
import chnSegment
import plotWordcloud


if __name__=='__main__':

    # 读取文件
    start = time.time()
    d = path.dirname(__file__)
    text = open(path.join(d, u'doc//lunwen.txt'), 'r', encoding='utf8').read()
    # text = open(path.join(d,'doc//alice.txt')).read()
    #  text="毕业快乐"

    # 若是中文文本，则先进行分词操作
    text=chnSegment.word_segment(text)
    # 生成词云
    plotWordcloud.generate_wordcloud(text)
    end = time.time()
    print(1)
