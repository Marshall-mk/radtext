from pathlib import Path
import pandas as pd

from radtext import csv2bioc
from tests import Example_Dir


def test_csv2bioc():
    file = Example_Dir / '1.csv'
    df = pd.read_csv(file, dtype=str)
    collection = csv2bioc.csv2bioc(df, 'ID', 'TEXT')
    assert len(collection.documents) == 2

    for i in range(1, 3):
        assert collection.documents[i-1].passages[0].text == df['TEXT'][i]
