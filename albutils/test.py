class Test():
    def __init__(self, name):
        self._name = name
        self._value = None
        self._has_passed = False

    def __str__(self):
        if self.value:
            return f"{self.name} - {self.has_passed} - {self.value}\n"
        return f"{self.name} - {self.has_passed}\n"

    @property
    def name(self):
        """The  property."""
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def has_passed(self):
        """The  property."""
        return self._has_passed
    @has_passed.setter
    def has_passed(self, value):
        self._has_passed = value

