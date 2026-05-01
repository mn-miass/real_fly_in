class display_testing():
    def __init__(self, nb_drones,
                 hub,
                 connection,
                 ignored,
                 invalid_lines,
                 comments,
                 empty_line,
                 is_valid):
    
        self.nb_drones = nb_drones
        self.hub = hub
        self.connection = connection
        self.comments = comments
        self.ignored = ignored
        self.empty_line = empty_line
        self.invalid_lines = invalid_lines
        self.is_valid = is_valid
        self._display()


    def _display(self):
        self.print_comment()
        self.print_ignored()
        self.print_hub()
        self.print_connection()
        self.empty_lines()
        self.others()
        self.print_invalid()

    def print_comment(self):
        print("=============comments===============")
        for comment in self.comments:
            print(f"{comment}: {self.comments[comment]}")

    def empty_lines(self):
        print("=========empty_lines=======")
        print(self.empty_line)
        print()


    def print_hub(self):
        print("==============hub==============")
        for element in self.hub:
            print(f"{element}: {self.hub[element]}")
        print()

    def print_ignored(self):
        print("==============ignored============")
        for element in self.ignored:
            print(f"{element}")
        print()

    def others(self):
        print("===========others===============")
        print(f"nb_drones: {self.nb_drones}")
        print(f"is_valid: {self.is_valid}")
        print()

    def print_connection(self):
        print("==============connection==============")
        for element in self.connection:
            print(f"{element}: {self.connection[element]}")
        print()

    def print_invalid(self):
        print("==============invalid==============")
        for element in self.invalid_lines:
            print(f"{element}")
        print()
