class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("****** Here is my int ******", args)
        print("****** Here is my cls ******", cls)
        print("****** Here is my kwargs ******", kwargs)
        
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwargs) ## usado para objetos precisam ser criados para classes já existentes
    
class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
    
i = int(4,5)