import requests
import re
import os

def crawl(keyword, save_path, num_images=250):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    num = 0
    list1 = []

    # Create a separate folder for each keyword
    keyword_folder = os.path.join(save_path, keyword)
    if not os.path.exists(keyword_folder):
        os.makedirs(keyword_folder)

    for i in range(num_images // 50):
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword + '&pn=' + str(i * 30)#You can choose according to your own situation
        res = requests.get(url, headers=headers)
        html1 = res.content.decode()
        a = re.findall('"objURL":"(.*?)",', html1)

        for b in a:
            try:
                if b not in list1:
                    num += 1
                    img = requests.get(b)
                    # Save the image to the keyword folder
                    with open(os.path.join(keyword_folder, keyword + str(num) + '.jpg'), 'wb') as f:
                        print(f'---------Downloading image number {num} for keyword "{keyword}"----------')
                        f.write(img.content)
                    list1.append(b)
            except Exception as e:
                print(f'---------Image number {num} for keyword "{keyword}" cannot be downloaded----------')
                continue
    print(f'Download completed for "{keyword}". Total images: {num}')

# List of food names
food_keywords = [
'waffle'
]

if __name__ == "__main__":
    save_path = "F://work//identification//Crawler"
    # Go through each food keyword and call the crawl function in turn to download
    for keyword in food_keywords:
        print(f'--- Starting download for keyword: "{keyword}" ---')
        crawl(keyword, save_path, num_images=250)



