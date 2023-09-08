import pandas as pd
reviews = pd.read_csv("./winer.csv", index_col=0)

#1

reviews_written = reviews.groupby('taster_twitter_handle').size()

# Check your answer
print(reviews_written)

#2

best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

# Check your answer
print(best_rating_per_price)

#3

price_extremes = reviews.groupby('variety').price.agg([min, max])

# Check your answer
print(price_extremes)

#4

sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

# Check your answer
print(sorted_varieties)

#5

reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# Check your answer
print(reviewer_mean_ratings)

#6

country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)

# Check your answer
print(country_variety_counts)