#!/bin/bash

# 读取文件
blog_path="~/Blog/source/_posts/"
blog_pic_path="~/Blog/source/images/"

loc_file_name="./"$1
echo "[*] get file "$1
loc_pic_path="./.$1/"

# 移动图片
echo "[*] copy file from $loc_file_name to $blog_path$1"
eval "cp $loc_file_name $blog_path"
echo "[*] copy picture from $loc_pic_path to $blog_path"
eval "cp -r $loc_pic_path $blog_pic_path/"

# 添加头属性
head=(
    "---"
    "title: $1"
    "date: 2021-06-15 17:01:37"
    "categories:"
    "tags:"
)

for line in ${head[*]}
do 
    eval "sed -i '1i\$line' $blog_path$1"
done