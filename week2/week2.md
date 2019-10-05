Data Processing
Python Panda Standardize Data
Data Normalization
Data Binning

Accessing Column Data Arrays With df[“column name”]

Dealing Missing Value
	check data source
	drop the missing value
		df.dropna(); inlace = true(modify the data frame directly)
	replace the missing data
		df.replace(missing_value, new_value)
		replace with an average
		replace by frequency
		replace by related functions
	leave it as missing Data

Data Formatting
Convert unit
Convert Abbreviation

df.rename(columns=:{“oldname”: “newname”}, inplace=True) — Rename Column Name

convert data types
Df.astype()

Data Normalization
Using statistic methods

Binning

Num.py
Bins = bp.linspace(misvalue, maxvalue, number of space number)
Group names = array[3]
df[“newcolumnname”] = pd.cut(column, bins, labels=Group names, include_lowest=True)

One Hot Encoding
panda.get_dummies(df[“column name”])
Data Wrangling