这个案例主要解决了爬虫获取动态页面的数据问题,使用了:
1.随机User-Agent中间件
2.selenium + PhantomJS
3.Tor的高匿代理
4.PhantomJS的页面渲染中间件
5.设置PhantomJS的随机User-Agent
6.解决了数据入库时带有单引号的问题