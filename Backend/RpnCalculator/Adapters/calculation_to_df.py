from typing import List

import pandas as pd
from Infrastructure.models import Calculation


def calculation_to_df(objs: List[Calculation]) -> pd.DataFrame:
    """Convert a SQLModel objects into a pandas DataFrame."""
    records = [i.dict() for i in objs]
    df = pd.DataFrame.from_records(records, index="id")
    return df.reindex(columns=["datetime", "equation", "result"])
