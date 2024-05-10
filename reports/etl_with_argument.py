"""
該報告使用main function, main function 會吃report_date + report_config(dict) 作為參數, 執行extract, transform, load
"""

import pandas as pd
from datetime import date


def extract(search_date: date, report_config: dict) -> pd.DataFrame:
    data = pd.DataFrame(
        {
            "id": range(100),
            "score": range(100),
            "date": pd.date_range(start=search_date, periods=100, freq="D"),
        }
    )

    return data


def transform(data):
    data["date"] = pd.to_datetime(data["date"])
    # add a new column year
    data["year"] = data["date"].dt.year
    return data


def load(data) -> None:
    data.to_csv("output/output3.csv", index=False)


def main(report_date: date, report_config: dict):
    data = extract(search_date=report_date, report_config=report_config)
    data = transform(data)
    load(data)


if __name__ == "__main__":
    report_config = {}
    report_date = date.today()
    main(report_date, report_config)
