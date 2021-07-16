from typing import Callable, List

from spacy.tokens import Doc, Span


def filter_with(
    keyword: str,
) -> Callable[[List[Doc]], List[Doc]]:
    def wrapper(
        docs: List[Doc],
    ) -> List[Doc]:
        return [doc for doc in docs if keyword in doc.text.lower()]

    return wrapper


filter_casino = filter_with("k8")


def to_sentences(
    docs: List[Doc],
) -> List[List[Span]]:
    return [list(doc.sents) for doc in docs]
