# -*- coding: utf-8 -*-
#!/usr/bin/python
#test_copyfile.py

import os,shutil

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分離檔案名稱與路徑
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #建立路徑
        shutil.move(srcfile,dstfile)          #移動檔案
        print ("move %s -> %s"%( srcfile,dstfile))

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分離檔案名稱與路徑
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #建立路徑
        shutil.copyfile(srcfile,dstfile)      #複製檔案
        print ("copy %s -> %s"%( srcfile,dstfile))

srcfile='C:\\Users\\jiunlin\\Desktop\\test.xlsx'
dstfile='C:\\Users\\jiunlin\\Desktop'

mycopyfile(srcfile,dstfile)
