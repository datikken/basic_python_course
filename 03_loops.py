# example working with loops
alp = ['a', 'b', 'c', 'd', 'e']


def while_loop_example():
    i = 0
    while i < len(alp):
        print('while res: ', alp[i], i)
        i += 1


while_loop_example()


def for_loop_example():
    for i in range(len(alp)):
        #print array elements with even index
        if i % 2 == 0:
            print('for res: ', alp[i], i)


for_loop_example()
