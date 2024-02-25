import pandas as pd


def extract(path = 'output.csv'):
    df = pd.read_csv(path, parse_dates=['date'])
    return df
 

def transform(data):
    data['month'] = data['date'].dt.month
    return data

def load(data) -> None:
    data.to_csv('output2.csv', index=False)

def etl():
    data = extract()
    data = transform(data)
    load(data)

if __name__ == "__main__":
    etl()