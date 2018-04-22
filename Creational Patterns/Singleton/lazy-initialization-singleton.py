class SingletonTest:
    _instance = None

    def __init__(self):
        if SingletonTest._instance is not None:
            print("This class has already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = SingletonTest()
        
        return cls._instance

if __name__ == "__main__":
    # Create the instances of class
    s = SingletonTest()
    # Get the instances multiple times, but all are the same instances.
    print(SingletonTest.getInstance())
    # Try to create a new instance, but failed.
    s = SingletonTest()
    # All instances are pointing to the same object.
    print(SingletonTest.getInstance())
