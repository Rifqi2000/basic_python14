# local scope
def myfunc():
    x = 100
    print(x)


myfunc()

#global scope

x = 1000


def myfuncs():
    x = 2000
    print(x)


myfuncs()
print(x)
