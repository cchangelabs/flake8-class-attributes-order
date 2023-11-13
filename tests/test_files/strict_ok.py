

class Foo:

    class Meta:
        a = 3

    CONSTANT = True

    def __init__(self):
        ...

    @property
    def bar(self):
        ...

    @bar.setter
    def bar(self, value):
        ...

    @bar.deleter
    def bar(self):
        ...

    @property
    def _bar(self):
        ...

    @_bar.setter
    def _bar(self, value):
        ...

    @_bar.deleter
    def _bar(self):
        ...


    @staticmethod
    def egg():
        ...

    @staticmethod
    def _egg():
        ...


    @classmethod
    def foobar(cls):
        ...

    @classmethod
    def _foobar(cls):
        ...
