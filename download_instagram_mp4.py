import requests,sys,time,re
import urllib.parse
from datetime import datetime
from tqdm import tqdm
#from urllib import request
#import requests
#import requests as req
#from urllib.request import Request, urlopen

#urlfb=str(sys.argv[1])
urlfb="https://www.instagram.com/reel/Ck5eiPugj0M/"
#urlfb="https://www.instagram.com/reel/CguUAaZFptq/?igshid=YmMyMTA2M2Y="


def scrap():
    print("start insta")
    data ={'url':urlfb}
    kimo0 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.post(url='https://ssyoutube.com/api/convert',data = data, headers=kimo0)
    time.sleep(2)
    #print(response.url)
    html=urllib.parse.unquote_plus(response.text)
    #print(html)

    #print("*******************************************************************************")
    
    raw_text = html
    start = 'uri='
    end = '&filename'
    
    #try:
    print("start titre")
    start_index = re.search(r'\b' + start + r'\b', raw_text).start()
    #print(start_index)
    end_index = re.search(r'\b' + end + r'\b', raw_text).end()
    trait_html = raw_text[start_index:end_index]
    #print(trait_html)
    size = len(trait_html)
    debut_char = trait_html[4:]
    size = len(debut_char)
    final_char = debut_char[:size - 9]
    #print(final_char)
    
    time.sleep(2)
    #print("*******************************************************************************")
    raw_text = html
    start = 'filename='
    end = '.mp4&'
    start_index = re.search(r'\b' + start + r'\b', raw_text).start()
    #print(start_index)
    end_index = re.search(r'\b' + end + r'\b', raw_text).end()
    trait_html_title = raw_text[start_index:end_index]
    #print(trait_html_title)
    
    size = len(trait_html_title)
    debut_char_title = trait_html_title[9:]
    size = len(debut_char_title)
    final_char_title = debut_char_title[:size - 5]
    print(final_char_title)
    time.sleep(2)
    download_video(final_char,"final_char_title")
    #except:
        #print("erreur")
        #time.sleep(2)
        #scrap()

def download_video(urll,final_char_title):

    print("Download Start")
    video_url =urll                                            #regex.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    locat_video="/data/data/com.termux/files/home/storage/shared/f_instagram/"#"C:\\Users\\ssd\Desktop\\download-main"#"/data/data/com.termux/files/home/storage/shared/f_instagram/"
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    with open(locat_video + final_char_title + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    print("downloaded successfully")

scrap()










'''
url = 'https://sssinstagram.com/request'

response = req.get(url)
print(response)
print("***********************************")
headers = response.headers
print(headers)
print("***********************************")
html = response.text
print(headers)
print("***********************************")

'''

'''
with open('code.txt', 'w', encoding="utf-8") as f:
    f.write(fbdown.decode('utf-8'))
'''

