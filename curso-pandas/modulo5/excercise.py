import pandas as pd
reviews = pd.read_csv("./winer.csv", index_col=0)

#1

dtype = reviews.points.dtype

# Check your answer
print(dtype)

#2

point_strings = reviews.points.astype(str)

# Check your answer
print(point_strings)

#3

missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
n_missing_prices = reviews.price.isnull().sum()

# Check your answer
print(n_missing_prices)

#4

reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)

# Check your answer
print(reviews_per_region)