# 项目说明
平常用到的爬虫，保存在一起，项目现在比较乱，后面需要整理

## 安装说明
1. 安装mongodb，用户数据存储
2. 使用python3.7,selenium

## qichacha爬虫
1. 已添加qichacha爬虫，整合selenium动态更新cookie
2. DownloadDelpay 设置为0，因为之前爬的太慢了，正常访问的时候，延迟需要放大
3. 由于qichacha限制，没有vip拉不到所有数据，又懒得登录，所以需要枚举search key ,目前采用人名枚举 
4. 爬虫depth设置为8
5. 刚找到了companyName可以用来替换qichacha查询的search key

## 其他爬虫方案
1. 使用crawlera管理ip代理
