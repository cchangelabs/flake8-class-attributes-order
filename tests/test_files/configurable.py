

class Foo:
    CONSTANT = 42

    field = 17

    class Meta:
        a = 3

    def __init__(self):
        ...

    @property
    def _egg(self):
        ...

    @_egg.setter
    def _egg(self, value):
        ...

    @property
    def egg(self):
        ...

    @egg.setter
    def egg(self, value):
        ...

    def bar(self):
        ...

    def _bar(self):
        ...

    def __str__(self):
        ...
