class Singleton:
    instance = None

    class __singleton:
        def __init__(self):
            pass

    def __init__(self):
        if Singleton.instance is None:
            Singleton.instance = Singleton.__singleton()

    # This functions is for test only.
    @classmethod
    def getInstance(cls):
        return cls.instance
