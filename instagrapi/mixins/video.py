import random
import time
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlparse
from uuid import uuid4
import requests,regex,sys
from urllib import request
from requests import Session
from datetime import datetime
from tqdm import tqdm

import requests

from instagrapi import config
from instagrapi.exceptions import (VideoConfigureError,VideoConfigureStoryError,VideoNotDownload,VideoNotUpload,)
from instagrapi.extractors import extract_direct_message, extract_media_v1
from instagrapi.types import (
    DirectMessage,
    Location,
    Media,
    Story,
    StoryHashtag,
    StoryLink,
    StoryLocation,
    StoryMedia,
    StoryMention,
    StorySticker,
    Usertag,
)
from instagrapi.utils import date_time_original, dumps


class DownloadVideoMixin:

    def video_download(self, media_pk: int, folder: Path = "") -> Path:

        media = self.media_info(media_pk)
        assert media.media_type == 2, "Must been video"
        filename = "{username}_{media_pk}".format(
            username=media.user.username, media_pk=media_pk
        )
        return self.video_download_by_url(media.video_url, filename, folder)

    def video_download_by_url(self, url: str, filename: str = "", folder: Path = "") -> Path:
        fname = urlparse(url).path.rsplit("/", 1)[1]
        filename = "%s.%s" % (filename, fname.rsplit(".", 1)[1]) if filename else fname
        path = Path(folder) / filename
        #response = requests.get(url, stream=True)
        #response.raise_for_status()
        #content_length = int(response.headers.get("Content-Length"))
        #file_length = len(response.content)

        file_size_request = requests.get(url, stream=True)
        file_size = int(file_size_request.headers['Content-Length'])
        block_size = 1024
        t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
        with open(path, 'wb') as f:#locat_video + filename + '.mp4'
            for data in file_size_request.iter_content(block_size):
                t.update(len(data))
                f.write(data)
            #t.close()
        '''
        if content_length != file_length:
            raise VideoNotDownload(f'Broken file "{path}" (Content-length={content_length}, but file length={file_length})')
        t = tqdm(total=content_length, unit='B', unit_scale=True, desc=filename, ascii=True)
        with open(path, "wb") as f:
            for data in file_size_request.iter_content(block_size):
            f.write(response.content)
            f.close()
        return path.resolve()
    '''
    def video_download_by_url_origin(self, url: str) -> bytes:

        response = requests.get(url, stream=True)
        response.raise_for_status()
        content_length = int(response.headers.get("Content-Length"))
        file_length = len(response.content)
        if content_length != file_length:
            raise VideoNotDownload(
                f'Broken file from url "{url}" (Content-length={content_length}, but file length={file_length})'
            )
        return response.content


def analyze_video(path: Path, thumbnail: Path = None) -> tuple:

    try:
        import moviepy.editor as mp
    except ImportError:
        raise Exception("Please install moviepy>=1.0.3 and retry")

    print(f'Analyzing video file "{path}"')
    video = mp.VideoFileClip(str(path))
    width, height = video.size
    if not thumbnail:
        thumbnail = f"{path}.jpg"
        print(f'Generating thumbnail "{thumbnail}"...')
        video.save_frame(thumbnail, t=(video.duration / 2))
    # duration = round(video.duration + 0.001, 3)
    video.close()
    return width, height, video.duration, thumbnail
