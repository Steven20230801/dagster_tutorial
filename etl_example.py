import pandas as pd

data = pd.DataFrame({
    "id": range(100),
    "score": range(100),
    "date": pd.date_range(start='1/1/2018', periods=100, freq='D')  
})
def extract():
    return data 

def transform(data):
    data['date'] = pd.to_datetime(data['date'])
    # add a new column year
    data['year'] = data['date'].dt.year
    return data

def load(data) -> None:
    data.to_csv('output.csv', index=False)

def etl():
    data = extract()
    data = transform(data)
    load(data)

if __name__ == "__main__":
    etl()