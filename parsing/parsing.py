from line_validator import LineValidator
from file_validator import FileValidator
from sys import argv
class Parsing():
    def __init__(self, path, permission):
        self.path = path
        self.permission = permission
        self.valid = True
        self.data = None
        self._validate()

    def _validate(self):
        file = FileValidator(self.path, self.permission)
        if file.valid == False:
            self.valid = False
        else:
            data = LineValidator(file.data)
            self.data = data.valid_lines
            self.comments = data.comments
            self.empty_line = data.empty_line



test = Parsing(argv[1], argv[2])
print (test.comments)
print(test.empty_line)
