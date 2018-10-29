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

# 只选取source和size1，source表示数据来源（天猫或京东）
sales = read_sql('select ShoeSize,ShoeColor from t_sales',engine)
# 过滤天猫胸罩销售数据，并按罩杯分组（size1字段），统计出每个罩杯的具体销量
tmallSize1GroupCount = sales.groupby('ShoeColor')['ShoeColor'].count()
# 计算出总销量
tmallSize1Total = tmallSize1GroupCount.sum()
print(tmallSize1Total)
# 将Series转换为DataFrame
tmallSize1 = tmallSize1GroupCount.to_frame(name='sales')
# 插入一个“比例”字段，用于显示销售比例
tmallSize1.insert(0,'proportion',100 * tmallSize1GroupCount / tmallSize1Total)
# 将索引名改成“罩杯”
tmallSize1.index.names=['size']
print(tmallSize1)

labels1 = []
labels1 = tmallSize1.index.tolist()
# for i in range(len(labels1)):
#     labels1[i] = labels1[i] + '码'
# 下面的代码会将天猫和京东的胸罩销售数据饼图放到同一个窗口显示
explode = [0,0,0,0.1,0,0,0,0,0,0]
patches, texts, autotexts = plt.pie(tmallSize1['sales'],explode=explode,labels=labels1,labeldistance=1.2,autopct='%.2f%%',pctdistance=0.8)
plt.title("中国男士鞋颜色分布",bbox={'facecolor':'white', 'pad':10},verticalalignment='bottom',loc ='left')
plt.legend()
plt.axis('equal')
# 重新设置字体大小
proptease = fm.FontProperties()
proptease.set_size('small')
# font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)
plt.show()