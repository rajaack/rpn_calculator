from datetime import datetime

from Backend.RpnCalculator.Adapters.calculation_to_df import calculation_to_df
from Backend.RpnCalculator.Infrastructure.models import Calculation


def test_calculation_to_df():
    date = datetime.now()
    calculation_db = Calculation(id=1, equation="1 1 +", result=2.0, datetime=date)
    df = calculation_to_df([calculation_db])

    assert len(df) == 1
    assert df.shape[0] == 1
    assert df.index[0] == 1
    assert df["equation"][1] == "1 1 +"
    assert df["result"][1] == 2.0
    assert df["datetime"][1] == date
