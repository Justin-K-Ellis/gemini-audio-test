from dataclasses import dataclass

@dataclass
class Monolog:
    no: int
    lesson_number: str
    type: str
    text: str
    speaker_gender: str