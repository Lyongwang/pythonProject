1、使用 git_group_url.py 先获取某个group（需要 groupId）下面的所有仓库地址。
	1）根据 git 权限不同，获取到的组不一样，默认使用大老师 git 的 token 来操作。
	2）获取到数据后，查找 groupId（Android：2554， iOS：2555）
	3）放入 excel主，让每个人修改仓库的主要分支。
2、使用 git_pull_porject.py 
	1）将所有项目拉取到某个目录下，它需要单独讲取一个文件，里面放了所有的 git地址和分支，需要空格分开。
3、使用 git_log_lines.sh 统计目录下的项目，将打印到控制台，复制内容到 excel 操作。
 	1）删除掉行数为空的用户
 	2）使用 =SUMIF(A$1:A$53,F1,d$1:d$53) 计算同一邮箱的所有的行数。
 	3）根据 email 推出用户的行数。