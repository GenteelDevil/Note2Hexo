# -*- coding:utf-8 -*-
import time
import shutil
import sys
import os
import re

if len(sys.argv) <= 1:
    print("Please input filename\n")
    sys.exit()

work_dir = os.getcwd()

loc_file_name = sys.argv[1]
loc_pic_name = "." + sys.argv[1] + "/"
print(loc_file_name)
print(loc_pic_name)

blog_file_path = '/home/oneshell/Blog/source/_posts' + loc_file_name
blog_pic_path = '/home/oneshell/Blog/source/images/'

# 复制文件和图片
print("[*] copy file from %s to %s" % (loc_file_name, blog_file_path))
shutil.copyfile(loc_file_name, blog_file_path)
print("[*] copy pictures from %s to %s" % (loc_pic_name, blog_pic_path))

pics = os.listdir(loc_pic_name)
for pic in pics:
    print("  [-] %s found" % pic)
    shutil.copyfile(loc_pic_name + pic, blog_pic_path + pic)

# 添加文件头
file_create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.stat(loc_file_name).st_ctime))
head_start = "---\ntitle: %s\ndate: %s" % (loc_file_name.split('.')[0], file_create_time)
categories = "\ncategories:"
for each in input("Categories: ").split(' ') : 
    categories += "\n- %s " % each
tags = "\ntags:"
for each in input("tags: ").split(' '):
    tags += "\n- %s" % each
head_end = "\n---\n"
head = head_start + categories + tags + head_end

# 修改图片链接
file_new = ""
file_new += head
with open(blog_file_path, "r") as f:
    for line in f:        
        # print(line)
        file_new += re.sub("(?<=\]\()\..*?\/", "/images/", line)
# print(file_new)
            

