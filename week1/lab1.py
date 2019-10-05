# import pandas library
import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)

print("The first 5 rows of the dataframe") 
df.head(5)

print("The last 10 rows of the dataframe\n")
df.tail(10)

#add headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers

#Drop Missing Value
df.dropna(subset=["price"], axis=0)

#print the name of columns
print(df.columns)

# check the data type of data frame "df" by .dtypes
print(df.dtypes)

#summary statistics
df.describe()
g
# describe all the columns in "df" 
df.describe(include = "all")

# look at the info of "df"
print(df.info)