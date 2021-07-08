import pandas
import toolz


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
