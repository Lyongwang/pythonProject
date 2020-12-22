#!/bin/bash
# declare -a array
list_alldir(){  
    for file2 in `ls -a $1`  
    do  
        if [ x"$file2" != x"." -a x"$file2" != x".." ];then  
            if [ -d "$1/$file2" ];then  
                # echo "$1/$file2"  
                # array[${#array[*]}] = "$1/$file2"
                # list_alldir "$1/$file2"  s
                cd "$1/$file2"
#                git log --format='%ae' | sort -u | while read email;
#                do
#                   echo "姓名:$email";
#                    git log --author="$email" --pretty=tformat: --since =='1990-01-01 00:00:00' --until='2020-12-15 23:59:59' --numstat |grep "\(|.java\|.gradle\|.xml\|.properties\|.pro\|.gitignore\|.py\|.sh\)$"| awk '{add += $1; subs += $2; loc += $1 - $2 } END { printf "%s,%s,%s,", add, subs, loc}' -;
                    git log --author="$email" --pretty=tformat: --since =='1990-01-01 00:00:00' --until='2020-12-15 23:59:59' --numstat -- . ":(exclude).git/" ":(exclude)pagetime/mappingtest.txt" ":(exclude)mapping.txt" ":(exclude)pagetime/mapping.txt" ":(exclude)pagetime/mapping3.txt" ":(exclude)oneTest/mapping.txt" | awk '{add += $1; subs += $2; loc += $1 - $2 } END { printf "%s",loc}' -;
#                    git log --author="$email" --pretty=tformat: --since =='1990-01-01 00:00:00' --until='2020-12-15 23:59:59' --numstat | awk '{add += $1; subs += $2; loc += $1 - $2 } END { printf "%s",loc}' -;
                    echo "#$file2"
#                    find . "(" -name "*.*" ")" -print | xargs wc -l
#                    echo "$file2"
#                    echo "$email";
#                done
            fi  
        fi  
    done  
}  
  
list_alldir /Users/lxiansheng/Downloads/temp-project/RN


# cd /Users/xuxiaolong/Downloads/temp-project/BFCommonLib
# git log --format='%ae' | sort -u | while read email; do echo -en "$email\t"; git log --author="$email" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done

