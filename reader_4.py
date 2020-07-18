import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        self.a = []
        try:
            with open(self.path, 'x'):
                pass
        except FileExistsError:
            with open(self.path, 'r') as f:
                self.a = f.read().splitlines()

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, new_str):
        self.new_str = new_str
        with open(self.path, 'w') as f:
            f.write(self.new_str)

    def __str__(self):
        return self.path

    def __iter__(self):
        for i in self.a:
            yield i
        return self

    def __add__(self, obj):
        storage_path = os.path.join(tempfile.gettempdir(), 'new_file.txt')
        new_obj = File(os.path.abspath(storage_path))
        with open(new_obj.path, 'w') as f:
            with open(self.path, 'r') as g:
                f.write(g.read())
            with open(obj.path, 'r') as g:
                f.write(g.read())
        return new_obj
