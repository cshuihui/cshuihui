import requests
import pixiv_id
import pixiv_image
import time
import os


def image_download(name, phpsessid, all_pages=1):
    save_dir = 'download'
    os.makedirs(save_dir, exist_ok=True)

    for pages in range(1, all_pages + 1):
        time.sleep(1)
        pid_list = pixiv_id.id_save(name, pages, phpsessid)
        time.sleep(1)
        link_list = pixiv_image.link_find(pid_list, phpsessid)

        print(f"正在下载第 {pages} 页的图片")
        headers = {
            "Referer": "https://www.pixiv.net/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/122.0.0.0 Safari/537.36",
        }

        for img_url in link_list:
            image_name = img_url.split(sep='/')[-1]
            print(f"正在下载 {image_name} ")
            time.sleep(1)

            try:
                response = requests.get(img_url, headers=headers, timeout=10)

                if response.status_code == 200:

                    with open(save_dir+'\\'+image_name, "wb") as f:
                        f.write(response.content)
                    print(image_name, '下载成功！')
                else:
                    print("请求失败", response.status_code)
            except requests.exceptions.Timeout:
                print("请求超时!")
            except requests.exceptions.RequestException as e:
                print(f"请求错误, 错误信息: {e}")


if __name__ == "__main__":
    phpsessid = "78166549_F5nPs6AxBOnQzd09d7wdEd5w63c94OSp"
    search_content = input('输入你要搜索的内容:')
    pages = int(input("输入总页数:"))
    image_download(search_content, phpsessid, all_pages=pages)
    print("下载完成！")
