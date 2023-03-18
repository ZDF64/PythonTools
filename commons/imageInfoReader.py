from importlib.metadata import files
import os
import shutil
import hashlib
from os import path
# 将QQ保存的图片导出到指定位置
def fun_file_scan(url,toDirUrl):
    files = os.listdir(url);
    for fs in files:
        real_url = path.join (url , fs)
        if path.isfile(real_url):
            print(os.path.basename(real_url),path.getsize(real_url));
            if os.path.basename(real_url).__contains__('jpg'):
                file_CopyTo(real_url,toDirUrl+"jpg\\")
            elif os.path.basename(real_url).__contains__('gif'):
                file_CopyTo(real_url,toDirUrl+"gif\\")
            elif os.path.basename(real_url).__contains__('png'):
                file_CopyTo(real_url,toDirUrl+"png\\")
            else:
                file_CopyTo(real_url,toDirUrl+"other\\")
        elif path.isdir:
            fun_file_scan(real_url,toDirUrl);
        else:
            print("unexception",real_url)
            pass
# 重命名
def file_rename(oldName,newName):
    print('rename')
    os.rename(oldName,newName);
# 复制
def file_CopyTo(fromUrl,toUrl):
    print('move')
    fpath,fname = os.path.split(fromUrl)
    Topath,Toname = os.path.split(toUrl)
    if not os.path.exists(Topath):
        os.makedirs(Topath)
    if not os.path.exists(fpath):
        print('The file is not Exist')
    # 名字转hashCode
    md5 = hashlib.md5()
    md5.update(fname.encode('utf-8'))
    toUrl = toUrl + md5.hexdigest() + '.' +fname.split('.')[1]
    shutil.copy(fromUrl,toUrl)
# fun_file_scan("C:\\Users\\ZDF64\\Documents\\Tencent Files\\1119054012\\Image\\Group2")
# fun_file_scan("E:\\qqImages","E:\\QQImagesDictionary\\")
fun_file_scan("C:\\Users\\ZDF64\\Documents\\Tencent Files\\1119054012\\Image\\Group2","E:\\QQImagesDictionary\\")