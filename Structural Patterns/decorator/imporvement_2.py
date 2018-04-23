# Change each common function with different validation of all projects that call it.
# If there are more projects in the future call the common function, more validation
# function are needed.

def proj1_validation():
    print('project 1 validation')

def proj2_validation():
    print('project 2 validation')

def proj3_validation():
    print('project 3 validation')

def f1():
    proj1_validation()
    proj2_validation()
    proj3_validation()
    print('f1')

def f2():
    proj1_validation()
    proj2_validation()
    proj3_validation()
    print('f2')

def f3():
    proj1_validation()
    proj2_validation()
    proj3_validation()
    print('f3')

def f4():
    proj1_validation()
    proj2_validation()
    proj3_validation()
    print('f4')

# Project 1
f1()
f2()
f4()

# Project 2
f2()
f3()
f4()

# Project 3
f2()
f3()
