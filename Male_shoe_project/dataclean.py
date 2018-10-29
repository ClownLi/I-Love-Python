"""
数据清理，整理鞋子的鞋码大小和颜色
"""

import sqlite3

conn = sqlite3.connect('/Users/limingzhu/Desktop/shoe1.sqlite')
c = conn.cursor()
print('Opened database')
# 增加一列ShoeSize
c.execute('alter table t_sales add column ShoeSize text;')
c.execute("update t_sales set ShoeSize = '35' where size like '%35%';")
c.execute("update t_sales set ShoeSize = '36' where size like '%36%';")
c.execute("update t_sales set ShoeSize = '37' where size like '%37%';")
c.execute("update t_sales set ShoeSize = '38' where size like '%38%';")
c.execute("update t_sales set ShoeSize = '39' where size like '%39%';")
c.execute("update t_sales set ShoeSize = '40' where size like '%40%';")
c.execute("update t_sales set ShoeSize = '41' where size like '%41%';")
c.execute("update t_sales set ShoeSize = '42' where size like '%42%';")
c.execute("update t_sales set ShoeSize = '43' where size like '%43%';")
c.execute("update t_sales set ShoeSize = '44' where size like '%44%';")
c.execute("update t_sales set ShoeSize = '45' where size like '%45%';")
c.execute("update t_sales set ShoeSize = '46' where size like '%46%';")
c.execute("update t_sales set ShoeSize = '47' where size like '%47%';")
c.execute("update t_sales set ShoeSize = '48' where size like '%48%';")
# 增加一列ShoeColor
c.execute("alter table t_sales add column ShoeColor text;")
c.execute("update t_sales  set ShoeColor = '黑色'  where color like '%黑%' ;")
c.execute("update t_sales  set ShoeColor = '绿色'  where color like '%绿%' ;")
c.execute("update t_sales  set ShoeColor = '红色'  where color like '%红%' ;")
c.execute("update t_sales  set ShoeColor = '白色'  where color like '%白%' ;")
c.execute("update t_sales  set ShoeColor = '蓝色'  where color like '%蓝%' ;")
c.execute("update t_sales  set ShoeColor = '粉色'  where color like '%粉%' ;")
c.execute("update t_sales  set ShoeColor = '卡其色'  where color like '%卡其%' ;")
c.execute("update t_sales  set ShoeColor = '米色'  where color like '%米%' ;")
c.execute("update t_sales  set ShoeColor = '沙色'  where color like '%沙%' ;")
c.execute("update t_sales  set ShoeColor = '灰色'  where color like '%灰%' ;")
conn.commit()
print('Operation done successfully')
conn.close()

