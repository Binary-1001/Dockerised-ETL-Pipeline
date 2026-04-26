import pandas as pd
import datetime as dt

def extract(file_path:str) -> pd.DataFrame:
    #Extarcting raw data from our flatfile
    print(f"\nExtracting data from {file_path}...\n")
    return pd.read_csv(file_path)

#print(extract("data/sales.csv").head())

def transform(df_raw:pd.DataFrame)-> pd.DataFrame:
    #calculate the total using quantity * price
    df_raw['total_amount'] = df_raw['quantity'] * df_raw['price']
    #convert date column in order_data using datetime method
    df_raw['order_date'] = pd.to_datetime(df_raw['order_date'])
    #standardise every region to uppercase
    df_raw['region'] = df_raw["region"].str.upper()
    #drop duplicates using drop_duplicates() method
    df_raw = df_raw.drop_duplicates(subset=["order_id"])

    return df_raw

print(transform(extract("data/sales.csv")))

def load():
    pass


def etl_pipeline():
    pass

if __name__ == "__main__":
    pass
