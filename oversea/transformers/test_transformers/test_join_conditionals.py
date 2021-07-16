import spacy.tokens

from oversea.transformers.join_conditionals import join_conditionals


def test_is_endofunctor(
    kraken_sentences,
):
    transformed = join_conditionals(kraken_sentences)

    assert isinstance(transformed, list)
    for sentence in transformed:
        isinstance(sentence, spacy.tokens.Span)


def test_first_sentence_is_a_fluff(kraken_sentences):
    action_keyword = "rzuć"
    [first, *transformed] = join_conditionals(kraken_sentences)

    assert action_keyword not in first.text.lower()


def test_second_sentence_has_action_keyword(kraken_sentences):
    action_keyword = "rzuć"
    [first, second, *transformed] = join_conditionals(kraken_sentences)

    assert action_keyword in second.text.lower()


def test_every_next_starts_with_number(kraken_sentences):
    [first, second, *transformed] = join_conditionals(kraken_sentences)

    for sentence in transformed:
        assert False
