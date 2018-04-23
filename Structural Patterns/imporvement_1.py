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
def proj1_validation_f1():
    print('project 1 validation f1')

def proj1_validation_f2():
    print('project 1 validation f2')

def proj1_validation_f4():
    print('project 1 validation f4')

proj1_validation_f1()
f1()
proj1_validation_f2()
f2()
proj1_validation_f4()
f4()

# Project 2
def proj2_validation_f2():
    print('project 2 validation f2')

def proj2_validation_f3():
    print('project 2 validation f3')

def proj2_validation_f4():
    print('project 2 validation f4')

proj2_validation_f2()
f2()
proj2_validation_f3()
f3()
proj2_validation_f4()
f4()

# Project 3
def proj3_validation_f2():
    print('project 3 validation f2')

def proj3_validation_f3():
    print('project 3 validation f3')

proj3_validation_f2()
f2()
proj3_validation_f3()
f3()
