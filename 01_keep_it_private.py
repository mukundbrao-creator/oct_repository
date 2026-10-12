class MyClass:
    __privateVar = 27
    
    def __privateMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("Private variable value:", MyClass.__privateVar)
foo = MyClass()
foo.hello()
foo.__privateMeth