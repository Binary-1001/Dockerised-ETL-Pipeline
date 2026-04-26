import pandas as pd 

def extract(file_path:str) -> pd.DataFrame:
    #Extarcting raw data from our flatfile
    print(f"\nExtracting data from {file_path}...\n")
    return pd.read_csv(file_path)

print(extract("data/sales.csv").head())

def transform():
    pass

def load():
    pass


def etl_pipeline():
    pass

if __name__ == "__main__":
    pass
