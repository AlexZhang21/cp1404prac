"""
CP1404/CP5632 Practical
Programming Language class with tests.
Estimate: 25 minutes
Actual:   20 minutes
"""

class ProgrammingLanguage:
    def __init__(self, name: str, typing: str, reflection: bool, year: int) -> None:
        self._name = name
        self._typing = typing
        self._reflection = reflection
        self._year = year

    @property
    def is_dynamic(self) -> bool:
        return self._typing == "Dynamic"

    def __str__(self) -> str:
        reflection_str = "True" if self._reflection else "False"
        return f"{self._name}, {self._typing} Typing, Reflection={reflection_str}, First appeared in {self._year}"
