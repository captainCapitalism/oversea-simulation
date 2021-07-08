import spacy


def load_nlp() -> spacy.Language:
    return spacy.load("pl_core_news_lg")
