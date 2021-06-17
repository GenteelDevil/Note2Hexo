# -*- coding:utf-8 -*-
import time
import shutil
import sys
import os
import re

if len(sys.argv) <= 1:
    print("Please input filename\n")
    sys.exit()

my_blog_base_path = "/home/oneshell/blog/blog/"

title = sys.argv[1].split('/')[-1].split('.')[0]

loc_file_path = os.path.abspath(sys.argv[1])
loc_pic_path = os.path.abspath(os.path.join(loc_file_path, os.path.pardir, '.' + title))
print(loc_file_path)
print(loc_pic_path)

blog_file_path = '/home/oneshell/Blog/source/_posts/' + title + '.md'
blog_pic_path = '/home/oneshell/Blog/source/images/'

# 复制文件和图片
print("[*] copy file from %s to %s" % (loc_file_path, blog_file_path))
shutil.copyfile(loc_file_path, blog_file_path)
print("[*] copy pictures from %s to %s" % (loc_pic_path, blog_pic_path))
try:
    pics = os.listdir(loc_pic_path)
    for pic in pics:
        print("  [-] %s found" % pic)
        shutil.copyfile(loc_pic_path + pic, blog_pic_path + pic)
except:
    print("  [-] No picture needed")

# 添加文件头
file_create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.stat(loc_file_path).st_ctime))
head_start = "---\ntitle: %s\ndate: %s" % (title, file_create_time)
categories = "\ncategories:"

for each in (loc_file_path.replace(my_blog_base_path, "").replace("/" + title + ".md", "").split('/')):
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
        file_new += re.sub("(?<=\]\()\..*?\/", "/images/", line)
with open(blog_file_path, 'w') as f:
    f.write(file_new)

            

