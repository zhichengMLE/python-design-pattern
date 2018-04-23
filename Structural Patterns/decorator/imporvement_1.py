# There is no need to change any code of common function
# Each project adds validation function before calling the
# common function.

def f1():
    print('f1')

def f2():
    print('f2')

def f3():
    print('f3')

def f4():
    print('f4')

# Project 1
def proj1_validation():
    print('project 1 validation')

proj1_validation()
f1()
proj1_validation()
f2()
proj1_validation()
f4()

# Project 2
def proj2_validation():
    print('project 2 validation')

proj2_validation()
f2()
proj2_validation()
f3()
proj2_validation()
f4()

# Project 3
def proj3_validation():
    print('project 3 validation')

proj3_validation()
f2()
proj3_validation()
f3()
