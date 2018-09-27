import pandas as pd
# Your code here
import pandas as pd
pd.set_option('max_rows', 5)
import numpy as np


reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#show the median and the mean
reviews.points.median()
reviews.points.mean()

#to pick all the countries without repetition
reviews.country.unique()
#countries appearing the most often
reviews.country.value_counts()
