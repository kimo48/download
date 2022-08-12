import youtube_dl
import sys
url=str(sys.argv[1])

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    video_title = info_dict.get('title', None)
    print(video_title.encode('unicode-escape').decode('utf-8'))
