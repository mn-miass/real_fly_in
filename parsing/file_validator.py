#tested evrythings works fine so far
#need to do the recovery for errors


class FileValidator():
    def __init__(self, path, permission) -> None:
        self.path = path
        self.permission = permission
        self.valid = True
        self.data = None
        self.error = ""
        self._validate()

    def _validate(self):
        try:
            with open(self.path) as file:
                if self.permission == "r":
                    self.data = file.readlines()
        except FileNotFoundError:
            self.error = "file not found"
            self.valid = False
        except IsADirectoryError:
            self.error = "is a directory"
            self.valid = False
        except PermissionError:
            self.error = "permission error"
            self.valid = False
        except UnicodeDecodeError:
            self.error = "unicode error"
            self.valid = False
        except UnicodeEncodeError:
            self.error = "unicode error"
            self.valid = False
        except OSError:
            self.error = "os error"
            self.valid = False
