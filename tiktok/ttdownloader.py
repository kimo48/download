from requests import Session
import re
from .utils import info_videotiktok
import requests

class TTDownloader(Session):
    BASE_URL = 'https://ttdownloader.com/'

    def __init__(self, url: str) -> None:
        super().__init__()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'dnt': '1',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'origin': 'https://ttdownloader.com',
            'referer': 'https://ttdownloader.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Linux",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest'
        }
        
        self.url = url

    def get_media(self):# -> list[info_videotiktok]:
        indexsource = self.get(self.BASE_URL)
        token = re.findall(r'value=\"([0-9a-z]+)\"', indexsource.text)
        #print("token: " ,token[0])
        #print(self.url)
        #print(self.BASE_URL)

        
        
        result = self.post(
            self.BASE_URL+'search/',
            data={'url': self.url, 'format': '', 'token': token[0]}
            )
        #print(result)
        
        nowm, wm, audio = re.findall(
            r'(https?://.*?.php\?v\=.*?)\"', result.text
        )
        #print(nowm)
        #print(wm)
        #print(audio)
        return [
            info_videotiktok(nowm, self, 'video'),
            info_videotiktok(wm, self, 'video', True),
            info_videotiktok(audio, self, 'music')
        ]


def ttdownloader(url: str):# -> list[info_videotiktok]:
    return TTDownloader(url).get_media()
