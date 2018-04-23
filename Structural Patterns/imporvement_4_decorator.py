# We can also use decorator which change nothing inner the code of common function.
# You can see the code below, we never change any code in the common function.
# We just add a decorator to each function.
# Learn more in this link: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html

def validation_center(func):
    def proj1_validation():
        print('project 1 validation')

    def proj2_validation():
        print('project 2 validation')

    def proj3_validation():
        print('project 3 validation')

    def decorator_call_this_function():
        proj1_validation()
        proj2_validation()
        proj3_validation()
        return(func())

    return decorator_call_this_function

@validation_center
def f1():
    print('f1')

@validation_center
def f2():
    print('f2')

@validation_center
def f3():
    print('f3')

@validation_center
def f4():
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
