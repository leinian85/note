[TOC]

### 1.版本控制工具
    git 分布式,没有中央服务器(每个节点都是中央服务器) 
    svn 集中式,必须有一个中央服务器

### 2.GIT
    配置:
    
- 配置用户名
> 会在/etc/下创建一个 gitconfig 的配置文件 
/etc/gitconfig
```
    e.g. 将用户名设置为Tedu
    $ sudo git config --system user.name Tedu
```   
- 配置用户邮箱
> 会在~/下创建一个 .gitconfig 的隐藏配置文件
~/.gitconfig 
```
    e.g. 将邮箱设置为lvze@tedu.cn
    $ git config --global user.email lvze@tedu.cn
```
- 配置编译器
```
    e.g. 配置编译器为pycharm
    $ git config core.editor pycharm
```
- 查看配置信息
```
    $ git config --list
```
    
### 3.基本命令
- 初始化仓库
>git init
意义：将某个项目目录变为git操作目录，生成git本地仓库。即该项目目录可以使用git管理

- 查看本地仓库状态
>git status

- 将工作内容记录到暂存区
>git add [files..]

- 将所有文件（不包含隐藏文件）记录到暂存区
>git add  *

- 取消文件暂存记录
>git rm --cached [file]

- 将文件同步到本地仓库
>git commit [file] -m [message]
说明: -m表示添加一些同步信息，表达同步内容

>e.g.  将暂存区所有记录同步到仓库区
git commit  -m 'add files'

- 查看commit 日志记录
>git log
git log --pretty=oneline

- 查看所有操作记录
>git reflog
注意:最上面的为最新记录，可以利用commit_id去往任何操作位置

- 比较工作区文件和仓库文件差异
>git diff [file]

- 将暂存区或者某个commit点文件恢复到工作区
>git checkout [commit] -- [file]
--是为了防止误操作，checkout还有切换分支的作用

- 移动或者删除文件
>git mv [file] [path]
git rm [files]
注意: 这两个操作会修改工作区内容，同时将操作记录提交到暂存区。

### 4 .gitignore 忽略文件
```
.gitignore忽略规则简单说明
file            表示忽略file文件
*.a             表示忽略所有 .a 结尾的文件
!lib.a          表示但lib.a除外
build/          表示忽略 build/目录下的所有文件，过滤整个build文件夹；
```

### 5.版本控制
- 退回到上一个commit节点
>git reset --hard HEAD^
注意 ： 一个^表示回退1个版本，依次类推。当版本回退之后工作区会自动和当前commit版本保持一致

- 退回到指定的commit_id节点
>git reset --hard [commit_id]


-创建标签
>标签: 在项目的重要commit位置添加快照，保存当时的工作状态，一般用于版本的迭代。

>git tag [tag_name] [commit_id] -m [message]
说明: commit_id可以不写则默认标签表示最新的commit_id位置，message也可以不写，但是最好添加。

>e.g. 在最新的commit处添加标签v1.0
git tag v1.0 -m '版本1'
查看标签
git tag 查看标签列表
git show [tag_name] 查看标签详细信息

- 去往某个标签节点
>git reset --hard [tag]

- 删除标签
>git tag -d [tag]

### 6.分支管理
定义: 分支即每个人在原有代码（分支）的基础上建立自己的工作环境，单独开发，互不干扰。完成开发工作后再进行分支统一合并。

- 查看分支情况
>git branch
说明: 前面带 * 的分支表示当前工作分支

- 创建分支
>git branch [branch_name]
说明: 基于a分支创建b分支，此时b分支会拥有a分支全部内容。在创建b分支时最好保持a分支"干净"状态。

- 切换工作分支
>git checkout [branch]

- 合并分支
>git merge [branch]

>冲突问题是合并分支过程中最为棘手的问题

>当分支合并时，原分支和以前发生了变化就会产生冲突
当合并分支时添加新的模块（文件），这种冲突可以自动解决，只需自己决定commit操作即可。
当合并分支时两个分支修改了同一个文件，则需要手动解决冲突。

- 删除分支
>git branch -d [branch] 删除分支
git branch -D [branch] 删除没有被合并的分支