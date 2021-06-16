#!/bin/bash

if [ $# == "0" ]; then
    echo "[!] No file name"
    exit
fi

# 读取文件
blog_path="~/Blog/source/_posts/"
blog_pic_path="~/Blog/source/images/"

loc_file_name="./"$1
echo "[*] get file "$1
loc_pic_path="./.$1/"

# 移动图片
echo "[*] copy file from $loc_file_name to $blog_path$1"
eval "cp $loc_file_name $blog_path"
echo "[*] copy picture from $loc_pic_path to $blog_path""images"
eval "cp -r $loc_pic_path $blog_pic_path/"

# 添加头属性

last_modify_timestamp=$(eval "stat -c %Y $1")
format_date=$(eval "date '+%Y-%m-%d\ %H:%M:%S' -d @$last_modify_timestamp")
head=(
    '---'
    'title: '$1
    "date:$format_date"
    'categories:'
    'tags:'
    '---'
)

eval "sed -i '1i\\\\n' $blog_path$1"
IFS=$'\n'
for line in ${head[*]}
do 
    echo $line
    eval "sed -i "1i\\$line" $blog_path$1"
done
unset IFS 

# 修改图片链接
# 1 获取文章中所有的图片超链接
eval "cat $blog_path$1" | while read line
do 
    echo $line
done
# 2 修改超链接名字