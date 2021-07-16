import pprint
from typing import List

from spacy.tokens import Span


def join_conditionals(sentences: List[Span]) -> List[Span]:
    pprint.pprint(sentences)
    fourth = sentences[3]
    print(dir(sentences[3][0]))
    return sentences
