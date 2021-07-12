import wordcloud
import functools
from matplotlib import pyplot


def make_word_cloud(
    words: str,
    stop_words,
    width: int = 1000,
    height: int = 500,
    show: bool = True,
):
    word_cloud = wordcloud.WordCloud(
        width=width,
        height=height,
        stopwords=stop_words,
    ).generate(words)
    if show:
        pyplot.imshow(word_cloud)
        pyplot.axis("off")
        pyplot.show()

    return word_cloud
