from enum import Enum


class PolarityCountPolarity(str, Enum):
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"

    def __str__(self) -> str:
        return str(self.value)
