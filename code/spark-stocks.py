# import necessary packages
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType, IntegerType
from pyspark.sql.window import Window
from pyspark.sql.functions import lit
import pandas as pd
import matplotlib.pyplot as plt

# create spark session
spark = SparkSession.builder.appName("StockData").getOrCreate()

# define stock schema (schema from csv file)
stock_schema = StructType([
    StructField('Date', TimestampType(), True),
    StructField('Open', DoubleType(), True),
    StructField('High', DoubleType(), True),
    StructField('Low', DoubleType(), True),
    StructField('Close', DoubleType(), True),
    StructField('Adj Close', DoubleType(), True),
    StructField('Volume', IntegerType(), True)
])

# Read in data from data directory
local_path = "./data/AAPL.csv" 
# Create apple stock data Spark DataFrame
apple_df = spark.read.format("csv").option("header", "true").schema(stock_schema).load(local_path)

# Create a pandas dataframe that holds the information from the apple dataframe
apple_pandas_df = apple_df.toPandas()
apple_pandas_df['Date'] = pd.to_datetime(apple_pandas_df['Date'])

# Create the visualization using matplotlib
plt.figure(figsize=(12, 6))
plt.plot(apple_pandas_df['Date'], apple_pandas_df['Close'], label='Close', c='red')
plt.plot(apple_pandas_df['Date'], apple_pandas_df['Adj Close'], label='Adjusted Close', c='blue')
plt.title('Close of AAPL')
plt.ylabel('Price')
plt.xlabel('Date')
plt.legend()
plt.grid(True)

# Save the plot to file
output_filename = "AAPL_Close_Plot.png"
plt.savefig(output_filename, dpi=300, bbox_inches='tight')