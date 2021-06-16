import time
import shutil
import sys
import os

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

# 修改图片链接