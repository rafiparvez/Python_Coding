

class Class:
    def add(self, x, y):
        return x+y

def not_add(x,y):
    return x*y

my_obj = Class()

my_obj.add = not_add

print(my_obj.add(3,4))


