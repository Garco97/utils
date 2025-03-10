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
