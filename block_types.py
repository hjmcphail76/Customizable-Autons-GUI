class GeneralBlock:
    def __init__(self, name):
        self.name = name


class TestBlockOne(GeneralBlock):
    def __init__(self, param1="default1", param2="default2"):
        super().__init__("Test Block One")
        self.param1 = param1
        self.param2 = param2


class TestBlockTwo(GeneralBlock):
    def __init__(self, param1="default3", param2="default4"):
        super().__init__("Test Block Two")
        self.param1 = param1
        self.param2 = param2
