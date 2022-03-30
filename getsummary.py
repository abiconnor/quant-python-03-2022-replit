#import pandas package
import pandas as pd

#load datafile and name
df_surveys = pd.read_csv("surveys.csv")

#summary statistics on weight column
desc_weight = df_surveys["weight"].describe()

#print summary stats
print(desc_weight)


