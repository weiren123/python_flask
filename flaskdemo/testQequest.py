import urllib.request

header={
"Host": "new.mp.di3sky.cn",
"Connection": "keep-alive",
"Content-Length": 16,
"Accept": "*/*",
"Origin": "http://new.mp.di3sky.cn",
"X-Requested-With": "XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Linux; Android 9; MIX 2S Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/45031 Mobile Safari/537.36 MMWEBID/8942 MicroMessenger/7.0.10.1580(0x27000A54) Process/tools NetType/WIFI Language/zh_CN ABI/arm64",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Referer": "http://new.mp.di3sky.cn/di3kpi/U-o4Bc402HJ7dVgSQFr4crQ5SkDNKQ/secKill?activityId=1277&refferId=22357967&urlRefferId=22425083&smsource=6",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,en-US;q=0.9",
"Cookie": "Secure; JSESSIONID=D2BE278D560213EA9776E4D05206385A; Secure; Secure"
}

# url 作为Request()方法的参数，构造并返回一个Request对象

request = urllib.request.Request("http://new.mp.di3sky.cn/di3kpi/activity/transmitRecord",headers=header)

# Request对象作为urlopen()方法的参数，发送给服务器并接收响应

response = urllib.request.urlopen(request)

html = response.read()
print(html)