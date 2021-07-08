from enum import Enum

PL_ENCODING = "UTF-16"


class Filenames(str, Enum):
    expeditions = "Karty Ekspedycji.csv"
    intrigues = "Karty intrygi.csv"
    goals = "Karty Celu.csv"
    magic = "Karty magii.csv"
