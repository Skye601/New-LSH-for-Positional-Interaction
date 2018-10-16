# git add
git add 命令可将该文件添加到缓存

# git status
git status 以查看在你上次提交之后是否有修改。

    $ git status
    On branch master

    Initial commit

    Changes to be committed:
    (use "git rm --cached <file>..." to unstage)

    new file:   README
    new file:   hello.php

# git  diff
执行 git diff 来查看执行 git status 的结果的详细信息。

git diff 命令显示已写入缓存与已修改但尚未写入缓存的改动的区别。git diff 有两个主要的应用场景。

尚未缓存的改动：git diff

查看已缓存的改动： git diff --cached

查看已缓存的与未缓存的所有改动：git diff HEAD

显示摘要而非整个 diff：git diff --stat

# git commit
使用 git add 命令将想要快照的内容写入缓存区， 而执行 git commit 将缓存区内容添加到仓库中

# git rm
删除文件

    $ git rm hello.php 
    rm 'hello.php'
    $ ls
    README