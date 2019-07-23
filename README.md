# StWeatherSpider

汕头2011年到2019年每一天的天气情况分析

## [点击进入目标网站](http://www.tianqihoubao.com/lishi/shantou/month/201101.html)

### 创建scrapy项目后先用shell调试工具抓取页面信息，页面返回200，可以使用scrapy“爬取”数据

之后再定义Item类，开发Spider类，使用Xpath从页面中提取每一天的天气信息，用这些信息来封装Item对象，最后开发Pipeline，处理Spider获取的Item对象，
可以先用print语句测试是否能在终端显示出爬取的数据。成功后再修改pipeline将爬取到的数据存入MySQL数据库，最后用Matplotlib生成含有最高气温与最低气温的
折线图

![Image text](https://github.com/Monarchh/StWeatherSpider/blob/master/StWeatherSpider/analysis/%E9%99%84/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-07-23%20%E4%B8%8B%E5%8D%8810.00.01.png)

通过Matplotlib里面的放大镜可以查看具体年份的气温情况（下图为2018年汕头气温情况）

![Image text](https://github.com/Monarchh/StWeatherSpider/blob/master/StWeatherSpider/analysis/%E9%99%84/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-07-23%20%E4%B8%8B%E5%8D%8810.00.41.png)

> * 操作系统：macOS Mojave

> * 时间：2019-7-23

> * 分析结果只代表时间段结果
