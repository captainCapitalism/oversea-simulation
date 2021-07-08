from typing import List

import pandas
import spacy
import toolz
from spacy import tokens


def remove_garbage(
    data: pandas.DataFrame,
) -> pandas.Series:
    return data["tekst"]


def rename_column(
    data: pandas.DataFrame,
) -> pandas.DataFrame:
    return data.rename({"tekst": "text"})


def transform(
    data: pandas.DataFrame,
) -> pandas.DataFrame:
    return toolz.pipe(
        data,
        remove_garbage,
        rename_column,
    )


def with_spacy(
    model: spacy.Language,
    data: pandas.DataFrame,
) -> List[spacy.tokens.Doc]:
    return [model(card) for card in data]
