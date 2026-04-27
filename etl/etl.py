import pandas as pd
from sqlalchemy import create_engine
import time


def extract(file_path:str) -> pd.DataFrame:
    #Extarcting raw data from our flatfile
    print(f"Extracting data from a trusted source system: {file_path}")
    return pd.read_csv(file_path)



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

def my_engine():
    engine = create_engine("sqlite:////data/pipeline_db.db")
    return engine

def load(file_db,df_transfromed:pd.DataFrame):
    #create an engine
    engine = my_engine()
    #load this cleaned to the database
    df_transfromed.to_sql(file_db, engine, if_exists='replace', index=False)
    
    return df_transfromed


def etl_pipeline():
    #Extraction stage
    print("ETL pipeline in progress.....\n")
    time.sleep(2)
    df_raw = extract("/data/sales.csv")
    print(f"\nExtraction of raw data is done here is a preview : \n{df_raw.head()}\n")
    

    #Transfromation stage
    print("\nTransforming raw messy data\n")
    time.sleep(2)
    df_transform = transform(df_raw)
    print(f"\nTransformation of raw messy data is done here is a preview : \n{df_transform.head()}\n")
    

    #Load stage
    print("\nLoading cleaned data into a database\n")
    time.sleep(2)
    quariable_data = load("sales",df_transform)
    print(f"\nLoading cleaned data into a database is complete here is a preview : \n{quariable_data.head()}\n")
    print("\nETL pipeline complete happy querying :) .....\n")

    
if __name__ == "__main__":
    etl_pipeline()
    print("\n")
    result = pd.read_sql("SELECT * FROM sales",my_engine())
    print("\nData in database:")
    print(result)
    print(f"\nTotal revenue: R{result['total_amount'].sum():,.2f}")
    print(f"Top region: {result.groupby('region')['total_amount'].sum().idxmax()}")
