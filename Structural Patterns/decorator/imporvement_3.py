# Define a common validation function which called by each common function.

def validation_center():
    def proj1_validation():
        print('project 1 validation')

    def proj2_validation():
        print('project 2 validation')

    def proj3_validation():
        print('project 3 validation')

    proj1_validation()
    proj2_validation()
    proj3_validation()

def f1():
    validation_center()
    print('f1')

def f2():
    validation_center()
    print('f2')

def f3():
    validation_center()
    print('f3')

def f4():
    validation_center()
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
