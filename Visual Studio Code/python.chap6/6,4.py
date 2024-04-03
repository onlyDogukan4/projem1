class Thing:
    def __init__(self):
        self._a = 1
        self._b = 4
    def foo(self, param):
        self._a = self._a + param
        self._b = self._b + param
        return (self._a + self._b)
    def bar(self, param):
        a = self._a + param
        b = self._b + param
        return (a + b)
    def __str__(self):
        return 'a is '+str(self._a)+', b is '+str(self._b)
    
it=Thing()

print(it.foo(2))
print(it.bar(3))
print(it)
