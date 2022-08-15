from user_pwd import Username,Password,Path
from instagrapi import Client
import sys
link=str(sys.argv[1])

def download_fn(link):
    try:
        print("Downlaod start")
        cl = Client()
        cl.login(Username, Password)
        info = cl.media_pk_from_url(link)
        clip_url = cl.media_info(info).video_url
        cl.clip_download_by_url(clip_url, folder = Path)
        print("Downlaod done")
    except:
        pass

download_fn(link)
