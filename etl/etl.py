import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import time
import os

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

#print(transform(extract("data/sales.csv")))

def load(df_transfromed:pd.DataFrame):
    #Warming up Postgres using time.sleep()
    time.sleep(6)
    #Setting up database data
    DB_HOST = os.environ.get('DB_HOST', 'postgres')
    DB_NAME = os.environ.get('DB_NAME', 'salesdb')
    DB_USER = os.environ.get('DB_USER', 'admin')
    DB_PASS = os.environ.get('DB_PASS', 'password')
    #create an engine
    engine = create_engine(f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')

    df_transfromed.to_sql("sales",engine,if_exists='replace',index=False)
    
    return df_transfromed

print(load(transform(extract("data/sales.csv"))))


def etl_pipeline():
    pass

if __name__ == "__main__":
    pass
