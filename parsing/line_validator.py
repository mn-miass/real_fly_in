import re

#comments = ["comment_num"] (comment, line)

class LineValidator():
    def __init__(self, data):
        self.data = data
        self.valid_lines = {}
        self.nb_drones = None
        self.invalid_lines = {}
        self.comments = {}
        self.empty_line = []
        self.is_valid = False
        self._validate()

    def _validate(self):
        self._get_comments()
        self._get_line()

    def _get_comments(self):
        pattern_comments = re.compile(r"[^#]*(#.*)")
        line_num = 1
        comment_num = 1
        for line in self.data:
            result = pattern_comments.match(line)
            if result:
                self.comments["comment_" + str(comment_num)] = (result.group(1), line_num)
                comment_num += 1
            line_num += 1


    def _get_line(self):
        pattern_empty_line = re.compile(r"^\s*$")
        line_num = 1
        for line in self.data:
            if pattern_empty_line.match(line):
                self.empty_line.append(line_num)
            line_num += 1

    def _get_drone_num(self):
        pattern_nb_drones = re.compile(r"\s*nb_drones\s*:\s*[+]*\s*(\d+)\s*")
        pattern_empty_line = re.compile(r"^\s*$")
        pattern_comments = re.compile(r"[^#]*(#.*)")

        for line in self.data:
            pass

    def _get_valide(self):
        pattern_nb_drones = re.compile(r"\s*nb_drones\s*:\s*[+]*\s*(\d+)\s*")
        pattern_end_hub = re.compile(r"\s*end_hub\s*:\s*([^\s]*)\s+(\d+)\s+(\d+)")
        pattern_start_hub = re.compile(r"\s*end_hub\s*:(\s*[^\s]*)\s+(\d+)\s+(\d+)")
        pattern_hub = re.compile(r"\s*hub\s*:\s*([^\s]*)\s+(\d+)\s+(\d+)")

        paterns = [pattern_start_hub,
                   pattern_end_hub,
                   pattern_hub]

    def _match_hub(self, line):
        pattern_hub = re.compile(r"\s*hub\s*:\s*([^\s]*)\s+(\d+)\s+(\d+)")
        result = pattern_hub.match(line)
        if result == True:
            return [result.group(1), result.group(2), result.group(3)]
        return None

    def _match_start_hub(self, line):
        pattern_start_hub = re.compile(r"\s*end_hub\s*:(\s*[^\s]*)\s+(\d+)\s+(\d+)")
        result = pattern_start_hub.match(line)
        if result == True:
            return [result.group(1), result.group(2), result.group(3)]
        return None

    def _match_end_hub(self, line):
        pattern_end_hub = re.compile(r"\s*end_hub\s*:\s*([^\s]*)\s+(\d+)\s+(\d+)")
        result = pattern_end_hub.match(line)
        if result == True:
            return [result.group(1), result.group(2), result.group(3)]
        return None
