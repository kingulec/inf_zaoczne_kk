class CMTest:
    def __init__(self,s):
        self.s = s
    def __enter__(self):
        print(f'enter {self.s}')
        return self
    def __exit__(self, x, y, z):
        print(f'exit {self.s}')

x = CMTest('Hello')

with x:
    print('Middle')