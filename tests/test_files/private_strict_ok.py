class Foo:
    CONSTANT = True

    @property
    def _bar(self):
        ...

    @_bar.setter
    def _bar(self, value):
        ...

    @_bar.deleter
    def _bar(self):
        ...

    @property
    def __bar(self):
        ...

    @__bar.setter
    def __bar(self, value):
        ...

    @__bar.deleter
    def __bar(self):
        ...

    @staticmethod
    def _egg():
        ...

    @staticmethod
    def __egg():
        ...

    @classmethod
    def foobar(cls):
        ...

    @classmethod
    def __foobar(cls):
        ...
