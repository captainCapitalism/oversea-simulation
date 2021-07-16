import os
import pickle

import pytest
import toolz
import functools

from oversea.nlp.load_nlp import load_nlp
from oversea.read import read_expeditions
from oversea import transformers
from oversea.transformers.filter_with import filter_casino, to_sentences


@pytest.fixture(scope="session")
def casino_sentences(expeditions_path):

    with open(expeditions_path, "rb") as f:
        serialized_data = pickle.load(f)
    return toolz.pipe(
        serialized_data,
        filter_casino,
        to_sentences,
    )


@pytest.fixture(scope="session")
def expeditions_path() -> str:
    return os.path.join(
        os.path.dirname((os.path.dirname(os.path.dirname(os.path.dirname(__file__))))),
        "data",
        "transformed",
        "expeditions.pkl",
    )


@pytest.fixture()
def kraken_sentences(casino_sentences):
    return casino_sentences[1]
