class SingletonTest:
    __instance = None

    def __init__(self):
        if SingletonTest.__instance is not None:
            print("This class has already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = SingletonTest()
        
        return cls.__instance

# Create the instances of class
s = SingletonTest()

# Get the instances multiple times, but all are the same instances.
print(SingletonTest.getInstance())
print(SingletonTest.getInstance())
print(SingletonTest.getInstance())
print(SingletonTest.getInstance())
# Try to create a new instance, but failed.
s = SingletonTest()
print(SingletonTest.getInstance())
print(SingletonTest.getInstance())
print(SingletonTest.getInstance())
print(SingletonTest.getInstance())