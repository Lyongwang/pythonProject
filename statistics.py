import os
import sys
import time

# from BeautifulReport import BeautifulReport


def invalid_format(start_day):
    try:
        time.strptime(start_day, "%Y-%m-%d")
        return True
    except:
        return False


def print_statistics(start_day):
    print(start_day)
    end_day = time.strftime("%Y-%m-%d", time.localtime())
    git_command = "git log --author=\"$(git config --get user.name)\" " \
                  "--pretty=tformat: --numstat --date=iso " \
                  "--since=" + start_day + "  --until=" + end_day + " " \
                  "| awk \'{ add += $1 ; subs += $2 ; loc += $1 - $2 } END " \
                  "{ printf \"added lines: %s removed lines : %s total lines: %s\",add,subs,loc }\'"
    print(git_command)
    result = os.popen(git_command)
    print(result.read())


if sys.argv[1] is None:
    print("开始时间不能为空!")
elif not invalid_format(sys.argv[1]):
    print("时间格式不正确(应为YYYY-mm-dd)")
else:
    print_statistics(sys.argv[1])
