import re

#comments = ["comment_num"] (comment, line)

class LineValidator():
    def __init__(self, data):
        self.data = data
        self.valid_lines = {}
        self.invalid_lines = {}
        self.comments = {}
        self.empty_line = []
        self._validate()

    def _validate(self):
        self._get_comments()
        self._get_line()

    def _get_comments(self):
        pattern_comments = re.compile(r"[^#]*(#.)")
        line_num = 1
        comment_num = 1
        for line in self.data:
            if pattern_comments.match(line):
                self.comments["comment_" + str(comment_num)] = (line, line_num)
                comment_num += 1
            line_num += 1


    def _get_line(self):
        pattern_empty_line = re.compile(r"\s+")
        line_num = 1
        for line in self.data:
            if pattern_empty_line.match(line):
                self.empty_line.append(line_num)
            line_num += 1

    def _get_valide(self):
        pattern_nb_drones = re.compile(r"")