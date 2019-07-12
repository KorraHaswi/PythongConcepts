#=============================================SCENARIO 1===============================================================
x=1
def foo():
    #x='salman'
    print(x)
    def koo():
        #x=3
        print(x)
    koo()
    return x

print(x)
print(foo())
print(x)

output
1
1
1
1
1
#==========================================SCENARIO 2=======================================================================
x=1
def foo():
    #x='salman'
    print(x)
    def koo():
        x=3
        print(x)
    koo()
    return x

print(x)
print(foo())
print(x)


output
1
1
3
1
1
#============================================SCENARIO 3=====================================================================


x=1
def foo():
    x='salman'
    print(x)
    def koo():
        x=3
        print(x)
    koo()
    return x

print(x)
print(foo())
print(x)

1
salman
3
salman
1
