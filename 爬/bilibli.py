import requests
from bs4 import BeautifulSoup

def search_bilibili(keyword):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.bilibili.com/",
    }

    # 构造搜索 URL
    url = "https://search.bilibili.com/all"
    params = {
        "keyword": keyword,
    }

    response = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    # 提取视频标题和链接
    results = []
    for a in soup.select("a.bili-video-card__wrap[href]"):
        title_tag = a.select_one("h3.bili-video-card__info--tit")
        if title_tag:
            title = title_tag.text.strip()
            link = "https:" + a["href"]
            results.append((title, link))

    return results

# 使用示例
if __name__ == "__main__":
    keyword = "纳西妲"
    videos = search_bilibili(keyword)
    for i, (title, link) in enumerate(videos, 1):
        print(f"{i}. {title}\n   {link}")
