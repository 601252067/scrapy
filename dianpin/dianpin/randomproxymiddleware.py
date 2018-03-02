# 代理中间件
class RandomProxyMiddleware(object):

    def process_request(self, request, spider):
        # ip = random.choice(self.proxy_list)
        # print(ip)
        request.meta['proxy'] = 'http://127.0.0.1:8123' # Tor高匿代理