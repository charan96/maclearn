import pandas as pd
import quandl

df = quandl.get("WIKI/GOOG")
print(df.head())
