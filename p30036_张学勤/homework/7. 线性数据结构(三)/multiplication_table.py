#!/usr/bin/env python3

# task1:
# 9 x 9 multiplication table


def original():
    for i in range(1, 10):
        for j in range(1, i + 1):
            fill_space = ' ' if j == 2 and i < 5 else ''
            print('{}*{}={}{}'.format(j, i, j * i, fill_space),
                  end='\n' if j == i else ' ')


# task2:
# multiplication table transform


# def right():
#     # join space version
#     for i in range(1, 10):
#         fill_space = ' ' * 7
#         print(fill_space * (i - 1), end='')
#         for j in range(i, 10):
#             print('{}*{}={:<2}'.format(j, i, j * i),
#                   end='\n' if j == 9 else ' ')

def right():
    # 'rjust' method version
    for i in range(1, 10):
        line = ''
        for j in range(i, 10):
            line += '{}*{}={:<2} '.format(i, j, i*j)
        # 64 --> first line length
        print(line.rjust(64))


right()


# task3:
# heart multiplication table
def heart():
    for i in range(1, 10):
        fill_space = ' ' * 3
        print(fill_space * (i - 1), end='')
        for j in range(i, 10):
            print('{}*{}={:<2}'.format(j, i, j * i),
                  end='\n' if j == 9 else ' ')
