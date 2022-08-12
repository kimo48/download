import requests,regex,sys,random
from urllib import request

urlfb=str(sys.argv[1])

UA = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Referer': 'https://fdown.net/',
'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie': '_ga=GA1.2.2094519438.1640138973; _gid=GA1.2.1078295655.1640138975; _gat_gtag_UA_44090370_1=1'}

fbdown = requests.post("https://fdown.net/download.php",data={"URLz": urlfb}, headers=UA).content
data="Download Video in Normal Quality"

if (data in fbdown.decode('ISO-8859-1')):
    RF = regex.findall('id="sdlink" href="(.*?)" download="',fbdown.decode('ISO-8859-1'))
    for DOWN in RF:
        CEK = DOWN.replace('amp;','')
    print(CEK)
#https://fb.watch/eR8HRRt5dp/
    
num_video=random.randrange(1000)

name_video=str(num_video)+".mp4"
locat_video="./storage/shared/Facebook/"+name_video

response = request.urlretrieve(CEK, locat_video)    

print("download complete")
