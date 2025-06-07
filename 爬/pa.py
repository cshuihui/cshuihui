import requests
import pandas as pd
url = "https://www.pixiv.net/users/78166549/bookmarks/artworks"
headers = {
    'referer': "https://www.pixiv.net/tags/nahida/artworks",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 "
                  "Safari/537.36 "
}
response = requests.get(url=url, headers=headers)
if response.status_code == 200:
    print(response.text)
    print("请求成功")
else:
    print("请求失败，错误码：", response.status_code)
# data = response.json()
# df = pd.DataFrame(data['data']['list'], columns=cols)
# print(df)
