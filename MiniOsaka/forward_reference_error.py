class A:
    def f(self):
        return B()

a = A()
a.f()  # NameError: name 'B' is not defined

b = B()  # NameError: name 'B' is not defined

def f():
    b = B()

f()  # NameError: name 'B' is not defined

class B:
    pass
