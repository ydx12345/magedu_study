## 安装git，win最简单，直接安装包就可以了，安装完成后在bash里进行操作


## 首先我们先创建一个文件夹，在git里被叫做是仓库

` mkdir learngit `这样我们就创建好了一个文件夹

`cd learngit ` 进入到这个文件夹中
- 然后把这个文件夹做成是git的仓库，使用的命令是 

` git init `
- 初始化后会创建一个.git的目录，这个目录会放一些与跟踪版本管理库相关的文件，切勿删除
- 接下里，编写一个文件，比如readme.txt,
- 然后，我们需要将这个文件添加到git的缓冲区中，用到的命令是

`git add readme.txt` 这样，这个文件就会被放到缓冲区中了
- 显然，在缓冲区中的文件并没有到最终的版本库中，我们需要进行提交，把它提交到版本库中
`git commit -m "描述信息` 每次提交必须带描述信息，这是一个好的习惯，在团队合作中才能更加和谐
- 在把文件放到缓冲区的时候，可以一次放入多个，而提交的操作是把缓冲区中的内容提交到版本库中。

## 让我们再试试

- 因为我们刚才已经把readme.txt放到版本库中了，那么我就来操作这个文件来试试
- 首先有个位置的概念，一共有四个地方，分别是
    - 工作区   当前文件夹
    - 缓冲区   用 git add <file> ，会把文件放到缓冲区 
    - 本地版本库区  用git commit -m "描述字符串"  会把文件放到本地版本库区
    - 远程服务器区  （等会就能学到了，别急）
- 我们修改工作区中的文件，如刚才创建的readme.txt，把里边加一句  "hello world"
- 然后我们使用命令
  

`git status`  此命令是查看当前git中的状态的，及其好用，不知道出现啥问题的时候，你就用这看
- 查看现在给出的信息，认真读，能看懂，他说的意思大概是，因为你现在对工作区的文件进行了修改，所以导致工作区的文件与版本库中的
- 文件不一样了，你可以使用 git add <file> 把你修改的文件放到缓冲区，或者，使用git checkout -- <file> 撤销刚才对工作区文件的修改
- 那么如何来查看那些东西变得不一样了呢，使用此命令
  

`git diff [file]`  如果写了file 那么将会显示两个文件的不同之处，如果没写，就会显示所有文件的不同之处，如果两个文件没区别，则啥也没有
    
- 你可以理解为，此仓库中的文件，其实是保留了两份，一份在工作区，另一份在版本库中，最好要保证两边的内容保持一致
- 当然，在你进行修改的时候两边一定会不一样，没有关系，正是因为这个缘故，无论你把那一边弄错了，都可以用另一边的来恢复
- 如果我们就是想把版本库中的文件进行更新，那么就在重复以前的操作，先放到缓冲区，然后在提交，就可以了
  
## 查看我们都做了那些提交的操作呢

- 使用此命令：

`git log`  将会显示已进行提交过的东西，那个id会很重要，留意他们的存在，当工作区的文件损坏或者丢失，可以用这些id来恢复
- 有时候，我们不需要看到这么详细的信息，那么我们只需要这么做，就可以看到更简短的信息了

`git log --pretty=oneling`  这样每个提交的信息就只会显示出一行了，分别是id跟当时提交的描述信息

- 当我们的版本需要回退的时候应该如何做呢？版本回退是退回第几次提交到版本库的意思，命令如下

`git reset --hard HEAD^` 这样表示退回到上一次提交，如果是HEAD^^这样就会退回到上两次提交，以此类推

- 注意这个HEAD，HEAD指的是当前你在的地方，就是你本人真正处于哪，慢慢理解

- 当然，这样做有时候太不方便了，我们可以这样做 HEAD~100， 那么这样就会退回到100次前进行的提交，我们就穿越回过去了
- 看着很美好，如果那样做，我们从我们穿越回来到现在的那么多次的提交都会消失，如果你没有记得以前的id号，那么你将无法在穿越回来**
- 试试上边的操作，然后再试试 git log 命令，你穿越到现在的那么多年的信息将全部消失掉，切记，穿越到过去时记住你要穿越回来的id

- 如果你想指定回到那个过去或者从过去回到未来，首先你要知道能确定的id号，然后进行如下操作

`git reset --hard ID` 那一大长串字符，其实只要复制一部分，只要能确定一条id 就可以进行穿越


- 刚才如果是误删了工作区的文件，也可以用此方法来回到没被破坏的时候，你只要用刚才的方法，让自己穿越回最后一次提交就可以
- 我想你应该会，试试操作下
## 没错，你还有后悔药的

- 当你的确没有记住你从哪年穿越到过去的时候，还有一个命令可以让你记起，你是什么年代穿越回来的
`git reflog` 这个命令会显示，你曾经都执行过哪些可能会涉及到穿越的时间线（id），
- 那么，其实说实话，你可以在任意的时间线进行穿梭了，试试玩玩
## 再说那几个位置

- 工作区，当前工作目录中除了.git目录之外的任何东西，都是工作区
- 缓冲区，这个可以简单的理解为一个内存中的结构，只是短暂的放一下要被提交的数据，等待着一起被提交
- 版本库，只会将文件从缓冲区中提交到版本库

- 理一下关系，工作区中的文件不能直接放入到版本库，必须首先放入到缓冲区，然后在从缓冲区到版本库中
## 关于回退以及撤销

- 撤销工作区的修改，变得和缓冲区的内容一样，如果缓冲区没有内容，那么将会和版本库中的内容一样，命令是

`git checkout -- <file>` 这样，就会撤销当前工作区的内容了

- 撤销提交到缓冲区的东西，命令是

`git reset HEAD <file>` 就会将提交到缓冲区的文件退回到工作区，以便再次修改后，在进行适当的操作

- 版本库撤销，也就是前边说过的穿越，命令是

`git reset --hard HARD~?` 回退到那个年代

`git reset --hard <id>` 回退到指定的某一年
## 删除文件

- 当然，其实你能直接删除的就是你工作区的文件，当你删除一个文件后，你可以使用命令

`git status`来比对当前工作区与版本库之间的差异，git会显示你们之间有哪些不同
- 这个时候就要看你到底想干什么了，比如你是因为错误操作，删错了文件，或者你是因为真的就像删除这个文件
- 如果你是因为错误操作而删除了文件，那么你还有后悔药，可以从版本库中把你曾经提交的文件在拖回来，命令是：

`git checkout -- <file>` git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”
- 另外一种就是你真的想删除那个文件了，你可以使用

`git rm <file>` 这样就会把这个file 文件删除了

--------------------------------------------
### 请小心，如果你直接使用 git rm  <file\> 的话会很危险，那会直接将版本库、工作区的文件全都干掉，那样就啥都没有了
## 在GitHub 上
- 首先请自行注册一个账号
- 在自己的家目录创建一个.ssh的目录
- 然后使用命令获取当前机器的ssh_key，命令如下：

`ssh-keygen -t rsa -C "youremail@example.com"` 邮箱你可以使用自己的邮箱，然后一路回车
- 然后回到你的家目录下的.ssh目录，看看这个目录下有没有id_rsa和id_rsa.pub这两个文件
- 这两个就是SSH Key的秘钥对，id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人。
- 登陆GitHub，打开“Account settings”，“SSH Keys”页面：然后，点“Add SSH Key”，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容
- 点“Add Key”，你就应该看到已经添加的Key
## 远程仓库

- 刚才为我们都是在本机创建的仓库，只能由本机使用，现在我们需要创建个远程仓库，为的是可以供大家使用，查看，克隆等等
- 在github上创建个仓库，你肯定会
- 创建完成后，发现这个仓库其实是空的，因为创建仓库就是相当于只是建了一个空文件夹而已，找到克隆和下载的按钮
- 会出现一个类似url的东西 git@github.com:your-name/仓库名.git，把它复制
- 好的，我们先回到我们本机的git仓库，我们输入这条命令：

`git remote add origin git@github.com:your-name/仓库名.git` 由于是第一次可能会出现 是否允许什么，yes就完事了，用人家东西就得相信人家
- 这样，我们本地的git仓库就与远端的仓库关联起来了，我们可以将本地的版本库推送至远端，命令如下

`git push -u origin master` 
- 把本地库的内容推送到远程，用git push命令，实际上是把当前分支master推送到远程。
- 由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。
- 然后在到github上，就会发现，本地版本库已经和远端的一模一样了
- 从现在起，只要本地提交后，就可以直接使用此命令推送到远端服务器上

`git push origin master` 把本地master分支的最新修改推送至GitHub origin仓库的master分支，现在，你就拥有了真正的分布式版本库！
## 依旧是远端仓库与本地版本库之间的操作

- 接下来，我们在github上创建一个新的仓库，并且我们勾选Initialize this repository with a README，这样GitHub会自动为我们创建一个README.md文件。创建完毕后，可以看到README.md文件
- 这样，我们就在远端创建好了一个新的仓库，仓库名为gitskill
- 点击克隆或下载的按钮，复制那个ssh的类似url的东西 如git@github.com:yourname/gitskills.git
- 接下来，我们在回到本地的git，我们将使用一个命令，把远端的仓库克隆到本地

`git clone git@github.com:yourname/gitskills.git` 这样，我们就把远端的仓库复制到本地了 
## 我们创建一个新的git仓库的分支

- 使用命令：

`git checkout -b <分支名>` git checkout 是切换分支的意思，-b是切换至一个新的分支，如果此分支存在，则无法切换，当分支存在就别用-b选项
- 此命令可以是分解为两个命令

`git branch <分支名>
 git checkout <分支名>
`
- 如何查看当前所在分支，只需要使用命令

`git branch` 会列出所有分支，在当前分支前边加上*

- 这样，我们在新分支里进行操作就不会影响到原来的分支了，当我们最后完成我们的所有操作后，我们可以将这两个分支进行合并

- 下面是对分支的描述，能帮助你更好的理解HEAD与分支

  ![image-20200331160539361](C:\Users\XHM\AppData\Roaming\Typora\typora-user-images\image-20200331160539361.png)

  

- 我们在分支里修改东西后，也需要进行提交到此分支的版本库，然后我们需要切换回原来的分支，准备进行合并的操作

- 接下来我们需要使用命令

`git merge <分支名>` 我们就可以把那个分支名的分支与当前所在的分支进行合并
- git merge命令用于合并指定分支到当前分支。合并后，再查看readme.txt的内容，就可以看到，和dev分支的最新提交是完全一样的。
- 注意到上面的Fast-forward信息，Git告诉我们，这次合并是“快进模式”，也就是直接把master指向dev的当前提交，所以合并速度非常快。
- 当然，也不是每次合并都能Fast-forward，我们后面会讲其他方式的合并。
- 合并完成后，就可以放心地删除dev分支了
- 删除分支需要的命令是:

`git branch -d dev` 这样就可以轻松地删掉分支了，然后我们在使用命令查看现在都有哪些分支

`git branch` 发现，现在只剩下master分支了

## 小结

- Git鼓励大量使用分支：

查看分支：`git branch`

创建分支：`git branch <name>`

切换分支：`git checkout <name>`或者`git switch <name>`

创建+切换分支：`git checkout -b <name>`或者`git switch -c <name>`

合并某分支到当前分支：`git merge <name>`

删除分支：`git branch -d <name>`