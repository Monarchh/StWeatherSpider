import mysql.connector
import re
from datetime import datetime
from matplotlib import pyplot as plt

# 用于提取最高温度和最低温度的具体数值
str_pat = re.compile(r'-?[\d]+[.]?[\d]*')

# 定义三个list列表作为展示的数据
dates, highs, lows = [], [], []

conn = mysql.connector.connect(user = 'root', password = '85757770', host = 'localhost', port = '3306', 
database = 'python', use_unicode = True)

cur = conn.cursor()

cur.execute("SELECT * FROM stweather")
# 将取得的序列（包含最高温和最低温）的值取出来
for row in cur:
    temp_high = str_pat.findall(row[3])[0]
    temp_low = str_pat.findall(row[3])[1]
    wdate = datetime.strptime(row[1], '%Y年%m月%d日')
    # 提取出来的值为字符串，转换成int类型
    highs.append(int(temp_high))
    lows.append(int(temp_low))
# 将数据库中的时间字符串进行时间格式化    
    dates.append(wdate)

# 配置图形
fig = plt.figure(dpi=128, figsize=(12, 9))
# 绘制最高气温的折线
plt.plot(dates, highs, c='red', label='最高气温', alpha=0.5, linewidth=1.0, linestyle='-', marker='v')
# 绘制最低气温的折线
plt.plot(dates, lows, c='blue', label='最低气温', alpha=0.5, linewidth=1, linestyle='-.', marker='o')
# 为两个数据的绘图区域填充颜色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置标题
plt.title("2011年1月至2019年7月汕头最高气温和最低气温")
# 为两个坐标轴设置名称
plt.xlabel("日期")
# 该方法绘制斜着的日期标签
fig.autofmt_xdate()
plt.ylabel("气温(℃)")
# 显示图例
plt.legend(loc='upper left')
plt.show()

