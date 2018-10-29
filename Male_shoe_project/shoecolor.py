#coding:utf-8
from matplotlib import font_manager as fm
from pandas import *
import matplotlib.pyplot as plt
import sqlite3
import sqlalchemy

# 打开数据库
engine = sqlalchemy.create_engine('sqlite:///shoe_clean.sqlite')
# rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format


sales = read_sql('select ShoeSize,ShoeColor from t_sales',engine)
tmallSize1GroupCount = sales.groupby('ShoeColor')['ShoeColor'].count()
tmallSize1Total = tmallSize1GroupCount.sum()
tmallSize1 = tmallSize1GroupCount.to_frame(name='sales')
tmallSize1.insert(0,'proportion',100 * tmallSize1GroupCount / tmallSize1Total)
tmallSize1.index.names=['size']
print(tmallSize1)

labels1 = []
labels1 = tmallSize1.index.tolist()
explode = [0,0,0,0.1,0,0,0,0,0,0]
patches, texts, autotexts = plt.pie(tmallSize1['sales'],explode=explode,labels=labels1,labeldistance=1.2,autopct='%.2f%%',pctdistance=0.8)
plt.title("中国男士鞋颜色分布",bbox={'facecolor':'white', 'pad':10},verticalalignment='bottom',loc ='left')
plt.legend()
plt.axis('equal')
proptease = fm.FontProperties()
proptease.set_size('small')
# font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)
plt.show()
