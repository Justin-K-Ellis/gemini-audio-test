from dataclasses import dataclass

@dataclass
class Dialog:
    text: str
    speaker1: str
    speaker1_gen: str
    speaker2: str
    speaker2_gen: str