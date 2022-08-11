#!/usr/bin/python

import sys
from tiktok import ttdownloader

d=ttdownloader(str(sys.argv[1]))

d[2].download('video.mp3')

#print (str(sys.argv[1]))
