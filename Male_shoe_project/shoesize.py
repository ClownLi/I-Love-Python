from matplotlib import font_manager as fm
from pandas import *
import matplotlib.pyplot as plt
import sqlite3
import sqlalchemy

# 打开数据库
engine = sqlalchemy.create_engine('sqlite:///shoe_clean.sqlite')
options.display.float_format = '{:,.2f}%'.format
sales = read_sql('select ShoeSize,ShoeColor from t_sales',engine)
tmallSize1GroupCount = sales.groupby('ShoeSize')['ShoeSize'].count()
tmallSize1Total = tmallSize1GroupCount.sum()
print(tmallSize1Total)
tmallSize1 = tmallSize1GroupCount.to_frame(name='sales')
tmallSize1.insert(0,'proportion',100 * tmallSize1GroupCount / tmallSize1Total)
tmallSize1.index.names=['size']
print(tmallSize1)
labels1 = []
labels1 = tmallSize1.index.tolist()
for i in range(len(labels1)):
    labels1[i] = labels1[i] + '码'
explode = [0,0,0,0,0,0,0,0.1,0,0,0,0,0,0]
patches, texts, autotexts = plt.pie(tmallSize1['sales'],explode=explode,labels=labels1,labeldistance=1.2,autopct='%.2f%%',pctdistance=0.7)
plt.title("中国男士鞋码大小分布",bbox={'facecolor':'white', 'pad':10, 'edgecolor' : 'black'},verticalalignment='bottom',loc ='left',color='black',fontsize='large',fontweight='bold')
plt.legend()
plt.axis('equal')
# 重新设置字体大小
proptease = fm.FontProperties()
proptease.set_size('small')
# font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)
plt.show()