### 打印上三角
def print_triangle1(n):
    lst = list(range(n, 0, -1))
    for i in range(n):
        print('{:>{}}'.format((' '.join([str(i)for i in lst[-i-1:]])), 2*n+n-10))

print_triangle1(10) # 20
print_triangle1(15) # 23
print_triangle1(30) # 

#------------------------------------------
### 打印下三角
def print_triangle2(n):
    lst = list(range(n, 0, -1))
    for i in range(n):
        print('{:>{}}'.format((' '.join([str(i)for i in lst[i:]])), 2*n+n-10))

print_triangle2(10)
print_triangle2(15)
print_triangle2(25)

