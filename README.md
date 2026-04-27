📦 Dockerised ETL Pipeline

A simple yet production-inspired ETL (Extract, Transform, Load) pipeline built with Python, Pandas, and SQLite. This project demonstrates how raw transactional data can be cleaned, transformed, and stored in a queryable database for analytics.

🚀 Project Overview

This project simulates a real-world data engineering workflow where messy sales data is:

Extracted from a CSV file
Transformed into a clean and usable format
Loaded into a relational database

The final dataset is then queried to generate basic business insights such as total revenue and top-performing region.

🧩 Architecture
data/sales.csv  -->  Extract  -->  Transform  -->  Load  -->  SQLite DB
                                                      |
                                                      v
                                               Business Insights
⚙️ Technologies Used
<p class="stack"> Python • Pandas • SQLAlchemy • SQLite • Docker (optional for containerisation) </p>
📂 Project Structure
.
├── data/
│   └── sales.csv          # Raw dataset
├── pipeline.py            # ETL pipeline script
├── pipeline_db.db         # SQLite database (generated)
├── requirements.txt
└── README.md



🔄 ETL Pipeline Breakdown

1. Extract
Reads raw data from a CSV file using Pandas
Source: data/sales.csv
df_raw = pd.read_csv(file_path)


2. Transform

Data cleaning and feature engineering:

✅ Calculates total_amount = quantity * price
✅ Converts order_date to datetime format
✅ Standardises region to uppercase
✅ Removes duplicate orders


3. Load

Loads transformed data into a SQLite database
Uses SQLAlchemy for database connection
Table name: sales
df.to_sql("sales", engine, if_exists="replace", index=False)


📊 Output & Insights

After running the pipeline:

📌 Data is stored in pipeline_db.db
📌 Queryable using SQL
📌 Example insights generated:
Total revenue: RXX,XXX.XX
Top region: REGION_NAME
▶️ How to Run
1. Install dependencies
pip install -r requirements.txt
2. Run the pipeline
python pipeline.py
🐳 Docker (Optional)

If containerised:

docker build -t etl-pipeline .
docker run etl-pipeline
💡 Key Learnings
Building modular ETL pipelines
Data cleaning with Pandas
Using SQLAlchemy for database operations
Structuring data workflows for scalability
🔮 Future Improvements
Add logging instead of print statements
Implement error handling & validation
Schedule pipeline (e.g., cron or Airflow)
Switch to PostgreSQL for production use
Add data quality checks