from line_validator import LineValidator
from file_validator import FileValidator
from sys import argv
# from tools import Zone, Connection
from diaplay_testing import display_testing



class Parsing():
    def __init__(self, path, permission):
        self.path = path
        self.permission = permission
        self.hub = {} #
        self.connection = {} #
        self.nb_drones = None #
        self.comments = {} #
        self.ignored = [] #
        self.invalid_lines = {} #
        self.empty_line = [] #
        self.valid = True #not yet
        self._validate()

    def _validate(self):
        file = FileValidator(self.path, self.permission)
        if file.valid == False:
            self.valid = False
        else:
            data = LineValidator(file.data)
            self.hub = data.hub
            self.comments = data.comments
            self.empty_line = data.empty_line
            self.nb_drones = data.nb_drones
            self.connection = data.connection
            self.ignored = data.ignored
            self.invalid_lines = data.invalid_lines
        

test = Parsing(argv[1], argv[2])
# print("comments")
# for comment, value in test.comments.values():
#     print(comment, value)
display_testing(test.nb_drones,
                test.hub,
                test.connection,
                test.ignored,
                test.invalid_lines,
                test.comments,
                test.empty_line,
                test.valid)
