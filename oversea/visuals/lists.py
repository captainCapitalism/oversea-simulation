from typing import Union, List

import plotly

from oversea.transformers import describe_sequence


def histogram(data: List[Union[int, float]]) -> plotly.graph_objs.Figure:
    fig = plotly.graph_objs.Figure(
        data=plotly.graph_objs.Bar(y=data),
    )
    description = describe_sequence.describe(data)

    fig.add_hline(
        description.median, annotation_text="median", annotation_position="bottom left"
    )
    fig.add_hline(
        description.mean, annotation_text="mean", annotation_position="top left"
    )
    fig.add_hline(
        description.mean + description.stdev,
        annotation_text="mean + stdev",
        annotation_position="top left",
    )
    fig.add_hline(
        description.mean - description.stdev,
        annotation_text="mean - stdev",
        annotation_position="top left",
    )
    fig.show()

    return fig
