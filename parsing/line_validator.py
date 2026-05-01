import re

#comments = ["comment_num"] (comment, line)
#valid_lines = {["type"]: {"name": str, "x": int, "y": int}}

class LineValidator():
    def __init__(self, data):
        self.hub_count = 0
        self.data = data
        self.hub = {}
        self.connection = {}
        self.nb_drones = None
        self.ignored = []
        self.valid_lines = []
        self.invalid_lines = []
        self.comments = {}
        self.empty_line = []
        self.is_valid = True
        self._validate()

    def _validate(self):
        line_num = 1
        _get = [self._get_comments,
                self._get_line,
                self._get_drone_num,
                self._get_start_hub,
                self._get_end_hub,
                self._get_hub,
                self._get_connection,
                self._get_invalid_lines]
        for line in self.data:
            for func in _get:
                func(line, line_num)
            line_num += 1


    def _get_comments(self, line, line_num):
        comment_num = len(self.comments)
        pattern_comments = re.compile(r"([^#]*)#(.*)")
        result = pattern_comments.match(line)
        if result:
            if result.group(2):
                self.comments["comment_" + str(comment_num)] = (result.group(2), line_num)
            else:
                self.comments["comment_" + str(comment_num)] = (result.group(1), line_num)

    def _get_line(self, line, line_num):
        pattern_empty_line = re.compile(r"^\s*$")
        result = pattern_empty_line.match(line)
        if result:
            self.empty_line.append(line_num)

    def _get_drone_num(self, line, line_num):
        pattern_nb_drones = re.compile(r"\s*nb_drones\s*:\s*(\d+)\s*")
        result = pattern_nb_drones.match(line)
        if result:
            if self.connection or self.hub or self.invalid_lines:
                self.ignored.append({"nb_drones should be at the first line": result[1], "line": line_num})
                self.is_valid = False
            elif self.nb_drones:
                self.ignored.append({f"nb_drones already exist {self.nb_drones} this will be skipped": result[1], "line": line_num})
            elif self.is_valid:
                self.nb_drones = result.group(1)

    def _get_start_hub(self, line, line_num):
        pattern_start_hub = re.compile(r"\s*start_hub\s*:(\s*[^\s]*)\s+(\d+)\s+(\d+)\s*(\[[^\]]*\])?")
        result = pattern_start_hub.match(line)
        if result:
            self.hub["start"] = {"name": result.group(1), "cordinates_x": result.group(2),
                                        "coordinates_y": result.group(3), "line": line_num, "metadata": result.group(4)}

    def _get_end_hub(self, line, line_num):
        pattern_end_hub = re.compile(r"\s*end_hub\s*:(\s*[^\s]*)\s+(\d+)\s+(\d+)\s*(\[[^\]]*\])?")
        result = pattern_end_hub.match(line)
        if result:
            self.hub["end"] = {"name": result.group(1), "cordinates_x": result.group(2),
                                        "coordinates_y": result.group(3), "line": line_num, "metadata": result.group(4)}

    def _get_hub(self, line, line_num):
        pattern_hub = re.compile(r"\s*hub\s*:(\s*[^\s]*)\s+(\d+)\s+(\d+)\s*(\[[^\]]*\])?")
        hub_num = len(self.hub)
        result = pattern_hub.match(line)
        if result:
            self.hub["hub_" + str(hub_num)] = {"name": result.group(1), "cordinates_x": result.group(2),
                                        "coordinates_y": result.group(3), "line": line_num, "metadata": result.group(4)}

    def _get_connection(self, line, line_num):
        pattern_connection = re.compile(r"\s*connection\s*:\s*([^\s]*)-([^\s]*)\s*(\[[^\]]*\])?")
        count_connection = len(self.connection)
        result = pattern_connection.match(line)
        if result:
            self.connection["connection_" + str(count_connection)] = {"hub_a": result.group(1), "hub_b": result.group(2), "line": line_num,
                                                                      "metadata": result.group(3)}
            count_connection += 1

    def _get_invalid_lines(self, line, num_line):
        pattern_comments = re.compile(r"([^#]*)#(.*)")
        pattern_empty_line = re.compile(r"^\s*$")
        pattern_empty_line = re.compile(r"^\s*$")
        pattern_start_hub = re.compile(r"\s*start_hub\s*:(\s*[^\s]*)\s+(\d+)\s+(\d+)")
        pattern_end_hub = re.compile(r"\s*end_hub\s*:(\s*[^\s]*)\s+(\d+)\s+(\d+)")
        pattern_hub = re.compile(r"\s*hub\s*:(\s*[^\s]*)\s+(\d+)\s+(\d+)")
        pattern_connection = re.compile(r"\s*connection\s*:\s*([^\s]*)-([^\s]*)")
        pattern_nb_drones = re.compile(r"\s*nb_drones\s*:\s*(\d+)\s*")

        check_list = [pattern_comments,
                      pattern_empty_line,
                      pattern_start_hub,
                      pattern_end_hub,
                      pattern_hub,
                      pattern_connection,
                      pattern_nb_drones]

        for element in check_list:
            result = element.match(line)
            if result:
                return
        self.invalid_lines.append({"data": line, "line": num_line})
