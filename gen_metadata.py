#-*- coding:utf-8 -*-
# 데이터 셋을 받았는데, 한글 인코딩이 CP949, UTF8으로 변환하고, <WAV:TEXT> 데이터 셋으로 변환 예정

import os, fnmatch
listOfFiles = os.listdir('.')
pattern = "*.txt"
store = []
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
    	print(entry)
        _fileName = open(entry,"r")
        if _fileName.mode == "r":
            content = _fileName.read()
            content = content.decode('cp949').encode('utf-8')
            print(content)