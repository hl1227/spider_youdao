import requests,pymongo,re,random,time,json,urllib3,hashlib,datetime,pymysql
from lxml import etree
urllib3.disable_warnings()

# def requ(url):
#     headers={'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
#              'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#              'Accept-Language': 'zh-CN,zh;q=0.9',}
#     username = "repackseo"
#     password = "sczokv3g"
#     a = requests.get(url, headers=headers, verify=False,timeout=3).content.decode()
#     pro_list=a.split('\n')
#     #pro_list=['123.169.123.26:9999', '175.43.153.145:9999', '191.97.7.99:999', '171.35.143.54:9999', '118.212.106.251:9999', '103.219.162.126:8080', '60.167.116.35:1133', '117.69.153.25:9999', '183.166.71.139:9999', '114.239.150.39:9999', '183.166.102.153:9999', '49.70.94.202:9999', '115.221.243.162:9999', '121.233.226.135:9999', '114.239.145.99:9999', '117.65.94.184:9999', '182.122.184.202:9999', '223.242.224.10:9999', '117.69.12.192:9999', '103.36.11.240:14571']
#     for proxy in pro_list:
#         proxy1 = {
#             "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy},
#             "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy}
#         }
#         print(proxy1)
#         try:
#             print(requests.get('https://httpbin.org/anything',timeout=5,verify=False,proxies=proxy1).content.decode())
#         except Exception as e:
#             print(e)
# requ('http://dps.kdlapi.com/api/getdps?orderid=911535952236358&num=1&sep=2')
#---------------------------------------------------------------
# for proxy in ['89.40.48.186:8080', '175.42.129.27:9999', '183.166.21.118:9999', '91.93.73.229:7070', '103.1.93.184:55443']:
#     proxy1={'http':'http://'+proxy,
#             'https':'https://'+proxy}
#     try:
#         requ('http://httpbin.org/ip',proxy1)
#     except Exception as e:
#         print(e)
#------------------------------------------------------------
# f = open('enForCrawl.txt', 'r', encoding='utf-8')
# l=f.readline().split(' ')
# print(l,len(l))


#-----------有道翻译-----------------
# content = 'Nita Ambani’s latest venture is a social media and networking platform for women – here’s a look at the organisations she runs as a part of Asia’s richest family'
# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# data = {}
# u = 'fanyideskweb'
# d = content
# time=time.time()*1000
# f = str(int(time) + random.randint(1,10))
# c = 'Tbh5E8=q6U3EXe+&L[4c@'
# sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
# data['i'] = content
# data['from'] = 'AUTO'
# data['to'] = 'AUTO'
# data['smartresult'] = 'dict'
# data['client'] = 'fanyideskweb'
# data['salt'] = f
#
# data['sign'] = sign
#
# data['doctype'] = 'json'
# data['version'] = '2.1'
# data['keyfrom'] = 'fanyi.web'
# data['action'] = 'FY_BY_CL1CKBUTTON'
# data['bv'] = '3d91b10fc349bc3307882f133fbc312a'
# data['lts']=f[:-1]
# headers={"Accept":"application/json, text/javascript, */*; q=0.01",
#          "Accept-Language":"zh-CN,zh;q=0.9",
#          "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#          "Cookie":#'OUTFOX_SEARCH_USER_ID=1179223152@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=486165313.7169691; _ntes_nnid=d37f109c7e9382d0a82cdbbd07b16dbd,1614847556602; JSESSIONID=abcXLCTBwCYzqdCWHjjHx; ___rl__test__cookies=1616136180435',
#                    "OUTFOX_SEARCH_USER_ID=1179223152@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=486165313.7169691; _ntes_nnid=d37f109c7e9382d0a82cdbbd07b16dbd,1614847556602; JSESSIONID=abcXLCTBwCYzqdCWHjjHx; ___rl__test__cookies={}".format(time),
#
#          "Referer":"http://fanyi.youdao.com/?keyfrom=dict2.top",
#          "Host":"fanyi.youdao.com",
#          "Origin":"http://fanyi.youdao.com","X-Requested-With":"XMLHttpRequest",
#          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
# proxies={'http':'http://183.151.91.221:17354'}
# print(requests.post(url,data=data,headers=headers,verify=False,proxies=proxies).status_code)
# pro={'https':'https://182.111.189.124:19902',
#      'http':'http://182.111.189.124:19902'}
# a=requests.post('http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule',data=data,proxies=pro).text
# print(a)
#--------------------
# proxy_url='http://dps.kdlapi.com/api/getdps?orderid=911535952236358&num=1&sep=2'
#print(requests.get('https://chinese.gratis/bible/index.php?q=&livre=&chapitre=1&verset=&Submit=Ok&action=recherche').text)
# print(datetime.datetime.now())
#--------------------------------------------------
# class A():
#     def __init__(self):
#         self.proxy=''
#         self.pro_time=datetime.datetime.now()
#         self.table_name = 'spider_proxy'
#         self.conn=self.__proxy_sql()
#         self.__get_ip()
#     def __proxy_sql(self):
#         conn = pymysql.Connect(
#             host='154.212.112.247',
#             port=13006,
#             # 数据库名：
#             db='seo-hy',
#             user="root",
#             passwd='itfkgsbxf3nyw6s1',
#             charset='utf8')
#         # cur = self.conn.cursor()
#         conn.autocommit(True)
#         print('代理数据库连接成功')
#         return conn
#         # 获取IP
#
#
#     def __get_ip(self):
#         cur = self.conn.cursor()
#         cur.execute('select http from {} where id = 1'.format(self.table_name))
#         self.proxy = cur.fetchone()[0]
#         print('======更新IP:', self.proxy,datetime.datetime.now())
#
#         # 判断是否更新IP
#     def update_proxy(self):
#         if datetime.datetime.now() > self.pro_time:
#             self.__get_ip()
#             self.pro_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
#     def run(self):
#         while True:
#             self.update_proxy()
#             time.sleep(5)
#             cur = self.conn.cursor()
#             cur.execute('select http from {} where id = 1'.format(self.table_name))
#             print('------',cur.fetchone()[0],datetime.datetime.now())
# A().run()
#-------------------------------------------------------------
# f = open(r'./bilingual_2021-0331.txt', 'r', encoding='utf-8')
# for word in f.readlines():
#     print(word.replace('\n',''))

a=[1,2,3,3,4,5]
b=0
for x in a:
    b=b+1
    if b ==b:
        print(888)