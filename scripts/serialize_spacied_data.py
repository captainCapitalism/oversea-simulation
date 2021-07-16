import functools
import pickle

import toolz
import os
from oversea import transformers
from oversea.nlp.load_nlp import load_nlp
from oversea.read import read_expeditions


def serialize_spacied_data() -> None:

    root_dir = os.path.dirname(os.path.dirname(__file__))
    target_dir = os.path.join(root_dir, "data", "transformed")
    targe_file = os.path.join(target_dir, "expeditions.pkl")
    data = toolz.pipe(
        read_expeditions(),
        transformers.expeditions.transform,
        functools.partial(transformers.expeditions.with_spacy, load_nlp()),
    )

    with open(targe_file, "wb") as f:
        pickle.dump(data, f)


if __name__ == "__main__":
    serialize_spacied_data()
