class Empty(Exception):
    def __init__(self, value='Empty Error') -> None:
        self.value=value
    def __str__(self) -> str:
        return(repr(self.value))
class OverFlow(Exception):
    def __init__(self, value='OverFlow Error') -> None:
        self.value=value
    def __str__(self) -> str:
        return(repr(self.value))
class UnderFlow(Exception):
    def __init__(self, value='UnderFlow Error') -> None:
        self.value=value
    def __str__(self) -> str:
        return(repr(self.value))
class size(Exception):
    def __init__(self, value='Size Error') -> None:
        self.value=value
    def __str__(self) -> str:
        return(repr(self.value))