import mechanize
from urllib.parse import unquote
import requests,regex,re,sys,random
from urllib import request
from datetime import datetime
from tqdm import tqdm
global CEK
CEK = "0000"

#url = 'https://www.facebook.com/reel/3389953797905979'
#url = 'https://fb.watch/hNHhv5Ialk/'
url =str(sys.argv[1])

br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]           # [('User-agent', 'Firefox')]
response = br.open(url)
data=response.read().decode('utf-8')
#print(data) 
#response1 = br.response() 
#i=response1.read()
'''
"a href="/video_redirect/?src=https"
&amp;source=misc&amp;id
a href="/video_redirect/?src=
'''
start_index = data.find('a href="/video_redirect/?src=https')
#print(start_index)
end_index = data.find('&amp;source=misc&amp;id')
#print(end_index)
trait_html = data[start_index:end_index]
link=unquote(trait_html)
link_f=(link.replace(r'a href="/video_redirect/?src=',""))

CEK =link_f
print(CEK)

def download_video(quality):
    """Download the video in HD or SD quality"""
    print(f"\nDownloading the video in {quality} quality... \n")
    video_url =CEK 
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    locat_video="/data/data/com.termux/files/home/storage/shared/f_Facebook/" #C:\\Users\\ssd\\Desktop\\download-main#/data/data/com.termux/files/home/storage/shared/f_Facebook
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    with open(locat_video + filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    print("\nVideo downloaded successfully.")

if CEK !="0000":
    download_video("SD")
else:
    print("\nVideo is private or not exsist")




