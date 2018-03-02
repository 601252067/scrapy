# -*- coding: utf-8 -*-

# Scrapy settings for it_juzi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'it_juzi'

SPIDER_MODULES = ['it_juzi.spiders']
NEWSPIDER_MODULE = 'it_juzi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'it_juzi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'it_juzi.middlewares.ItJuziSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 该中间件将会收集失败的页面，并在爬虫完成后重新调度
   #'scrapy.downloadermiddlewares.retry.RetryMiddleware': 80,
   #  'Crawler.comm.rotate_useragent.RotateUserAgentMiddleware' :400
   'it_juzi.middlewares.RotateUserAgentMiddleware': 200,
   'it_juzi.middlewares.RandomProxyMiddleware':300,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'it_juzi.pipelines.ItJuziPipeline': 300,
   #'scrapy_redis.pipelines.RedisPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



# log日志
# LOG_FILE = "juziSpider.log"
# LOG_LEVEL = "INFO"




# 支持随机下载延迟
# RANDOMIZE_DOWNLOAD_DELAY = True



# 使用了scrapy-redis里的去重组件，不使用scrapy默认的去重
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了scrapy-redis里的调度器组件，不实用scrapy默认的调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 使用队列形式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 允许暂停，redis请求记录不丢失
# SCHEDULER_PERSIST = True
# redis链接
# REDIS_HOST = "127.0.0.1"
# REDIS_PORT = 6379
