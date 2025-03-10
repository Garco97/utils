import socket

NET=0
LOCAL=1
class Printer():
    def __init__(self, mode, ip, port, path):
        self.mode = mode
        if self.mode == NET:
            try:
                self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.conn.connect((ip, port))
            except Exception as e:
                print(f"Error with the printer {e}")
                return
        elif self.mode == LOCAL:
            self.conn = open(path, "w")
        else:

            pass
    def send_print(self, cmd):
        if self.mode == NET:
            self.conn.sendall(cmd.encode())
        elif self.mode == LOCAL:
            self.conn.write(cmd)
        else:
            pass

    def close(self):
        self.conn.close()


class Test():
    def __init__(self, name):
        self._name = name
        self._value = None
        self._has_passed = False

    def __str__(self):
        return f"{self.name} - {self.has_passed} - {self.value}\n"

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

