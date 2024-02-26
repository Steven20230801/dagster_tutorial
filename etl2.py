import time
import pandas as pd


def extract(path="output.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    return df


def transform(data):
    data["month"] = data["date"].dt.month
    return data


def load(data) -> None:
    print("sleeping for 10 seconds from load")
    time.sleep(2)
    data.to_csv("output2.csv", index=False)


def etl():
    data = extract()
    print("sleeping for 3 seconds from etl")
    time.sleep(3)
    data = transform(data)
    load(data)


if __name__ == "__main__":
    etl()
