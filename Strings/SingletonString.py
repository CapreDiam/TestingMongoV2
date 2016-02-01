class SingletonString:
    w = "fff"

    class __SingletonString:

        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not SingletonString.instance:
            SingletonString.instance = SingletonString.__SingletonString(arg)
        else:
            SingletonString.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)
