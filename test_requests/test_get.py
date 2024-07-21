import requests



r = requests.get('https://api.github.com/events')

print(r.status_code)    # 返回状态码
print(r.json())         # 返回json
print(r.text)           # 返回text文本
