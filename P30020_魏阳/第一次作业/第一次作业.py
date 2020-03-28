#### 打印 9*9乘法表
#1
for i in range(1,10):
    for j in range(1,i+1):
        print("{} * {} = {:2}".format(j,i,i*j),end='\n' if i == j else ' ')

#2
for i in  range(1,10):
    for j in range(1,i+1):
        line = "{} * {} ={:2} ".format(j,i,i*j)
        print(line,end="")
    print()
#3 
for i in  range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}{}".format(j,i,i*j,  ' ' if j==2 and i < 5 else ''), #第四个括号{}，是判断前3行后面加空格用的
              end='\n' if i == j else ' ')
#### 打印菱形
#1
for i in range(-3,4):
    if i < 0:
        i = -i
    print(' '* i + (7-(2*i))* '*')
#2

n = int(input("请输入数字："))
e = n // 2
for i in range(-e,n-e):
    print("{:^{}}".format('*'*(n-2*abs(i)),n))  # :^{}是把字符串居中

#### 打印100以内的斐波拉契数列，求第101项
#1
a = 0
b = 1
index = 0
print('fib({}) = {}'.format(index,a))
print('fib({}) = {}'.format(index,b))
while  True:
    c = a + b
    index += 1
    print('fib({}) = {}'.format(index,c))
    if index == 101:
        break
    a = b
    b = c

#2
p = int(input("请输入要查询的斐波拉契项数："))
index = 1
a, b = 0, 1
while  index < p:
    c = a + b
    #print(c)     打印具体项数
    a, b = b, a + b
    index += 1
print(c)
##### 求10w以内的素数
#1  效率很低，重复计算量大
count = 0
for x in range(2,100000):
    for i in range(2,x):
        if x % i == 0:#合数
            break
    else:#
        #print(x)
        count +=1
print(count)
#2 利用开平方 大大的降低重复俩
count = 0
for x in range(2,100000):
    for i in range(2,int(x ** 0.5)+1):  ## 没想到（x** 0.5） +1，没有理解
        if x % i == 0:#合数
            break
    else:#
        #print(x)
        count +=1
print(count)
#3 利用range函数跳过偶数
count = 1
print(2)
for x in range(3,100000,2):
    for i in range(3,int(x ** 0.5)+1,2):
        if x % i == 0:#合数
            break
    else:#
        #print(x)
        count +=1
print(count)

#4 大于10 能被5整除的
count = 1
print(2)
for x in range(3,100000,2):
    if x > 10 and x % 5 == 0:
        continue
    for i in range(3,int(x ** 0.5)+1,2):
        if x % i == 0:#合数
            break
    else:#
        #print(x)
        count +=1