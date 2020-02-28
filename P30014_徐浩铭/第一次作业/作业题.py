# author: 徐浩铭 time: 2020.2.28
### 九九乘法表
# 第一种实现
def nine():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f"{j}*{j}={j*i:^2}\t",end="")
        print()

# 第二种实现
def nine2():
    for i in range(1,10):
        str1 = ''
        for j in range(1, i+1):
            str1 += f'{j}*{i}={i*j:^2}\t'
        print(str1)

# 我认为第二种实现更好一点，IO次数会少很多，只有9次，应该效率会高一点，不过这两种
# 的时间复杂度都是O(n²)。

### 打印菱形
def print_diamond(m=6):
    for i in range(1, m):
        print(f"{' '*(m-i)}{'*'*(i*2-1)}")
    for j in range(1, m-1):
        print(f"{' '*(j+1)}{'*'*((m-j-1)*2-1)}")
# 先打上三角，然后再打下三角

### 100以内的斐波那契数列
def fib(n=100):
    pre, nex = 0, 1
    for i in range(n):
        if nex > n:
            break
        print(nex)
        nex, pre = nex+pre, nex

### 求斐波那契数列的第101项
def fib2(n=101):
    pre, nex = 0, 1
    for i in range(n):
        nex, pre = nex+pre, nex
    print(pre)


### 10万以内的所有素数
# 第一种
def calculate(n=100000):
    print(2, end='\t')
    for i in range(3, n, 2):
        flag = True
        for j in range(3, int(i ** 0.5)+1, 2):
            if not i % j:
                flag = False
                break
        if flag:
            print(i, end="\t")
# 基本的优化点用上了，就一下一下迭代，除的开就直接扔
# 第二种
def calculate2(n=100):
    lst = [2]
    for i in range(3, n, 2):
        flag = True
        for j in lst:
            if j > i ** 0.5:
                break
            if not i % j :
                flag = False
        if flag:
            lst.append(i)
    print(lst)

# wayne老师说还有更Nb的，应该是还有别的算法了，这个效率应该还凑活

