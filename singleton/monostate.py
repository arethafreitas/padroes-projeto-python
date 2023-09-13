## Primeira forma

# class Borg:
#     __shared_state = {"1": "2"}
#     def __init__(self):
#         self.x = 1
#         self.__dict__ = self.__shared_state
#         pass

# b = Borg()
# b1 = Borg()
# b.x = 4

# print("Borg Objetct 'b':", b) ##b e b1 são objetos distintos
# print("Borg Object 'b1': ", b1)

# print("Object State 'b':", b.__dict__) ##b e b1 são objetos que compartilham o mesmo estado
# print("Object State 'b1':", b1.__dict__)


## Segunda forma
class Borg(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
    
b = Borg()
b1 = Borg()
b.x = 4

print("Borg Objetct 'b':", b) ##b e b1 são objetos distintos
print("Borg Object 'b1': ", b1)

print("Object State 'b':", b.__dict__) ##b e b1 são objetos que compartilham o mesmo estado
print("Object State 'b1':", b1.__dict__)
